import requests
from PyQt6.QtWidgets import QWidget
from frontend.src.designers.login import Ui_LoginForm
from frontend.src.services.reqister_form import RegisterForm

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

