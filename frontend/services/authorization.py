import requests
from PyQt6.QtWidgets import QWidget

from designers.login import Ui_LoginForm
from designers.register import Ui_RegisterForm
from frontend.services.contacts import ContactSelectorWindow


class LoginForm(QWidget, Ui_LoginForm):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButtonLogin.clicked.connect(self.user_login)
        self.pushButtonRegister.clicked.connect(self.redirect_to_register_form)

    def user_login(self):
        username_form = self.lineEditLogin.text()
        password_form = self.lineEditPassword.text()
        data = {
            'username': username_form,
            'password': password_form
        }
        token = requests.post('http://127.0.0.1:8000/api/token/', data=data)
        if 'access' in token.text and 'refresh' in token.text:
            f = open('frontend/config.txt', mode='w')
            f.write(token.json()['access'])
            self.redirect_to_contacts_form()
        print(token.text)

    def redirect_to_register_form(self):
        self.close()
        self.register_form = RegisterForm()
        self.register_form.show()
        print('registerrrr')

    def redirect_to_contacts_form(self):
        self.close()
        self.contacts_form = ContactSelectorWindow()
        self.contacts_form.show()


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

        token = requests.post('http://127.0.0.1:8000/api/register/', data=data)
        # if 'blank' not in token.text:
        #     self.redirect_to_login_form()
        print(token.text)

    def redirect_to_login_form(self):
        self.close()
        self.login_form = LoginForm()
        self.login_form.show()
