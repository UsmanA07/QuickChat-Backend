import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget
from src.designers.login import Ui_LoginForm


class LoginForm(QWidget, Ui_LoginForm):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.login_btn = self.pushButtonLogin.clicked.connect(self.get_acces_token)

    def get_acces_token(self):
        self.username_form = self.lineEditLogin.text()
        self.password_form = self.lineEditPassword.text()
        data = {
            'username': self.username_form,
            'password': self.password_form
        }

        tokens = requests.post('http://127.0.0.1:8000/api/token/', data=data)
        print(tokens.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginForm()
    ex.show()
    sys.exit(app.exec())
