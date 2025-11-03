import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QHBoxLayout, QLabel, QVBoxLayout
from frontend.designers.chat import Ui_ChatWindow
import requests


class ChatWindow(QWidget, Ui_ChatWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
