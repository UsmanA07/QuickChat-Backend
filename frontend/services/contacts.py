import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QHBoxLayout, QLabel, QVBoxLayout
from frontend.designers.chat import Ui_ContactSelector
import requests


class ContactSelectorWindow(QWidget, Ui_ContactSelector):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.get_contacts_for_api()

    def init_ui(self):
        self.setupUi(self)
        self.listWidgetContacts.itemClicked.connect()

    def get_contacts_for_api(self):
        contacts = requests.get('http://127.0.0.1:8000/api/users-list/')
        # for contact in contacts.json():
        #     print(contact['username'])
        for contact in contacts.json():
            item = QListWidgetItem(contact["username"])
            # item.setData(QtCore.Qt.UserRole, contact)
            self.listWidgetContacts.addItem(item)
    def hello(self):
        print('111111111111111')


def main():
    app = QApplication(sys.argv)
    window = ContactSelectorWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
