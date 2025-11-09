import asyncio
import requests
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QThread, pyqtSignal, QObject

from centrifuge import *
from config import UsernameManager
from designers.login import Ui_LoginForm
from designers.register import Ui_RegisterForm
from frontend.services.contacts import ContactSelectorWindow
from frontend.config import TokenManager


class CentrifugeWorker(QThread):
    finished_signal = pyqtSignal()
    error_signal = pyqtSignal(str)

    def __init__(self, client, subscription):
        super().__init__()
        self.client = client
        self.subscription = subscription
        self._should_stop = False

    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            loop.run_until_complete(self._run_async())
            loop.close()
        except Exception as e:
            self.error_signal.emit(str(e))

    async def _run_async(self):
        try:
            await self.subscription.subscribe()
            await self.client.connect()
            print(f"Subscription state: {self.subscription.state}")
            print(f"Subscription channel: {self.subscription.channel}")

            while not self._should_stop:
                await asyncio.sleep(0.1)

        except Exception as e:
            self.error_signal.emit(str(e))
        finally:
            self.finished_signal.emit()

    def stop(self):
        self._should_stop = True


class UserLoginWorker(QThread):
    login_success = pyqtSignal(str)
    login_failed = pyqtSignal(str)

    def __init__(self, login_form):
        super().__init__()
        self.login_form = login_form

    def run(self):
        try:
            username_line = self.login_form.lineEditLogin.text()
            password_line = self.login_form.lineEditPassword.text()
            data = {
                'username': username_line,
                'password': password_line
            }
            response = requests.post('http://127.0.0.1:8000/api/token/', data=data)
            print(response.status_code)

            if response.status_code == 200 and 'access' in response.text:
                self.login_form.manager.save_token(response.json()['access'])
                self.login_form.username_manager.save_username(username_line)
                self.login_success.emit(username_line)
            else:
                error_msg = "Login failed"
                if response.status_code != 200:
                    error_msg = f"Server error: {response.status_code}"
                self.login_failed.emit(error_msg)

        except Exception as e:
            self.login_failed.emit(f"Connection error: {str(e)}")


class LoginForm(QWidget, Ui_LoginForm):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.manager = TokenManager()
        self.username_manager = UsernameManager()
        self._centrifuge_worker = None
        self.client = None

    def init_ui(self):
        self.setupUi(self)
        self.pushButtonLogin.clicked.connect(self.user_login)
        self.pushButtonRegister.clicked.connect(self.redirect_to_register_form)

        self.login_worker = UserLoginWorker(self)
        self.login_worker.login_success.connect(self.on_login_success)
        self.login_worker.login_failed.connect(self.on_login_failed)

    def user_login(self):
        self.pushButtonLogin.setEnabled(False)
        self.pushButtonLogin.setText("Logging in...")
        self.login_worker.start()

    def on_login_success(self, username):
        self.pushButtonLogin.setEnabled(True)

        self.subscribe_to_self(username)
        self.redirect_to_contacts_form()

    def on_login_failed(self, error_msg):
        self.pushButtonLogin.setEnabled(True)
        self.pushButtonLogin.setText("Login")
        print(f"Login error: {error_msg}")

    def redirect_to_register_form(self):
        self.close()
        self.register_form = RegisterForm()
        self.register_form.show()

    def redirect_to_contacts_form(self):
        self.close()
        self.contacts_form = ContactSelectorWindow()
        self.contacts_form.show()

    def subscribe_to_self(self, username):
        self.client = Client(
            "ws://127.0.0.1:8001/connection/websocket",
            get_token=self.manager.get_token,
            use_protobuf=False,
        )

        sub = self.client.new_subscription(
            channel=f'user:{username}',
        )

        self._centrifuge_worker = CentrifugeWorker(self.client, sub)
        self._centrifuge_worker.start()

    def closeEvent(self, event):
        if self._centrifuge_worker and self._centrifuge_worker.isRunning():
            self._centrifuge_worker.stop()
            self._centrifuge_worker.wait(1000)

        if self.login_worker and self.login_worker.isRunning():
            self.login_worker.quit()
            self.login_worker.wait(1000)

        super().closeEvent(event)


class RegisterForm(QWidget, Ui_RegisterForm):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButtonRegister.clicked.connect(self.user_register)
        self.pushButtonLogin.clicked.connect(self.redirect_to_login_form)

    def user_register(self):
        username_form = self.lineEditUsername.text()
        email_form = self.lineEditEmail.text()
        password_form = self.lineEditPassword.text()
        data = {
            'username': username_form,
            'email': email_form,
            'password': password_form
        }

        try:
            response = requests.post('http://127.0.0.1:8000/api/register/', data=data)
            if response.status_code == 200:
                print("Registration successful")
            else:
                print(f"Registration failed: {response.status_code}")
        except Exception as e:
            print(f"Registration error: {e}")

    def redirect_to_login_form(self):
        self.close()
        self.login_form = LoginForm()
        self.login_form.show()
