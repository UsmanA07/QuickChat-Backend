from PyQt6.QtWidgets import QListWidgetItem, QWidget
import requests
from centrifuge import Client

from services.config import *
from designers.contacts import Ui_ContactSelector
from services.chat import ChatWindow


class ContactSelectorWindow(QWidget, Ui_ContactSelector):
    def __init__(self):
        super().__init__()
        self.token_manager = TokenManager()
        self.recipient_username = RecipientManager()
        self.username = UsernameManager()
        self.init_ui()
        self.get_contacts_for_api()

    def init_ui(self):
        self.setupUi(self)
        self.listWidgetContacts.itemClicked.connect(self.redirect_to_chat)

    def get_contacts_for_api(self):
        contacts = requests.get('http://127.0.0.1:8000/api/users/list/')
        for contact in contacts.json():
            item = QListWidgetItem(contact["username"])
            self.listWidgetContacts.addItem(item)

    def redirect_to_chat(self, item):
        self.recipient_username.save_username(item.text())
        print(item.text())
        print(self.recipient_username.get_username_sync())
        self.close()
        self.chat_window = ChatWindow()
        self.chat_window.show()

    def sort_id_services(self):
        return '_'.join(sorted([self.recipient_username.get_username_sync(), self.username.get_username_sync()]))
