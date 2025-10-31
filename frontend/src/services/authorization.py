import requests
from PyQt6.QtWidgets import QWidget
from frontend.src.designers.login import Ui_LoginForm
from frontend.src.designers.register import Ui_RegisterForm


class LoginForm(QWidget, Ui_LoginForm):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButtonLogin.clicked.connect(self.get_access_token)
        self.pushButtonRegister.clicked.connect(self.redirect_to_register_form)

    def get_access_token(self):
        self.username_form = self.lineEditLogin.text()
        self.password_form = self.lineEditPassword.text()
        data = {
            'username': self.username_form,
            'password': self.password_form
        }
        tokens = requests.post('http://127.0.0.1:8000/api/token/', data=data)
        print(tokens.text)

    def redirect_to_register_form(self):
        self.close()
        self.register_form = RegisterForm()
        self.register_form.show()


class RegisterForm(QWidget, Ui_RegisterForm):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.login_btn = self.pushButtonRegister.clicked.connect(self.user_register)
        self.redirect_to_login_btn = self.pushButtonLogin.clicked.connect(self.redirect_to_login_form)

    def user_register(self):
        self.username_form = self.lineEditUsername.text()
        self.email_form = self.lineEditEmail.text()
        self.password_form = self.lineEditPassword.text()
        data = {
            'username': self.username_form,
            'email': self.email_form,
            'password': self.password_form
        }

        tokens = requests.post('http://127.0.0.1:8000/api/register/', data=data)
        print(tokens.text)

    def redirect_to_login_form(self):
        self.close()
        self.login_form = LoginForm()
        self.login_form.show()
