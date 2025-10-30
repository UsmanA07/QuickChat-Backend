import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget
from src.designers.register import Ui_RegisterForm


class RegisterForm(QWidget, Ui_RegisterForm):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.login_btn = self.pushButtonLogin.clicked.connect(self.get_acces_token)

    def get_acces_token(self):
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegisterForm()
    ex.show()
    sys.exit(app.exec())
