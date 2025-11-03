import sys
from PyQt6.QtWidgets import QApplication

from frontend.services.authorization import LoginForm

def main():
    app = QApplication(sys.argv)
    ex = LoginForm()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
