import sys

from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QHBoxLayout, QLabel, QVBoxLayout

from config import UserTokenManager
from designers.contacts import Ui_ContactSelector
from services.chat import ChatWindow
from PyQt6.QtCore import Qt
import requests


class ContactSelectorWindow(QWidget, Ui_ContactSelector):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.get_contacts_for_api()
        self.manager = UserTokenManager()

    def init_ui(self):
        self.setupUi(self)
        self.listWidgetContacts.itemClicked.connect(self.redirect_to_chat)

    def get_contacts_for_api(self):
        contacts = requests.get('http://127.0.0.1:8000/api/users/list/')
        for contact in contacts.json():
            item = QListWidgetItem(contact["username"])
            self.listWidgetContacts.addItem(item)

    def redirect_to_chat(self, item):
        username = item.text()
        print(username)
        headers = {
            "Authorization": f"Bearer {self.manager.get_token_sync()}"
        }
        data = {
            'recipient': username,
            'sender': self.manager.get_token_sync()
        }
        r = requests.post('http://127.0.0.1:8000/api/chat/', headers=headers, data=data)
        print(r.status_code)
