import requests
from PyQt6.QtWidgets import QWidget
from frontend.src.designers.register import Ui_RegisterForm


class RegisterForm(QWidget, Ui_RegisterForm):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.login_btn = self.pushButtonLogin.clicked.connect(self.user_register)

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

