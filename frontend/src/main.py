import sys
from PyQt6.QtWidgets import QApplication

from frontend.src.services.login_form import LoginForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginForm()
    ex.show()
    sys.exit(app.exec())
