import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QHBoxLayout, QLabel, QVBoxLayout
from frontend.designers.contacts import Ui_ContactSelector
from frontend.services.chat import ChatWindow
from PyQt6.QtCore import Qt
import requests


class ContactSelectorWindow(QWidget, Ui_ContactSelector):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.get_contacts_for_api()

    def init_ui(self):
        self.setupUi(self)
        self.listWidgetContacts.itemClicked.connect(self.redirect_to_chat)

    def get_contacts_for_api(self):
        contacts = requests.get('http://127.0.0.1:8000/api/users-list/')
        for contact in contacts.json():
            item = QListWidgetItem(contact["username"])
            self.listWidgetContacts.addItem(item)

    def redirect_to_chat(self, item):
        username = item.text()
        print(username)
        token = open('frontend/config.txt').readline()
        headers = {
            "Authorization": f"Bearer {token}"
        }
        data = {
            'recipient': username,
        }
        r = requests.post('http://127.0.0.1:8000/api/send/', headers=headers, data=data)
        print(r.status_code)

# def main():
#     app = QApplication(sys.argv)
#     window = ContactSelectorWindow()
#     window.show()
#     sys.exit(app.exec())
#
#
# if __name__ == '__main__':
#     main()
