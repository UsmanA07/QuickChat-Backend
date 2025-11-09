from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QHBoxLayout, QLabel, QVBoxLayout
import requests


from config import TokenManager, RecipientManager
from designers.contacts import Ui_ContactSelector
from services.chat import ChatWindow


class ContactSelectorWindow(QWidget, Ui_ContactSelector):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.get_contacts_for_api()
        self.manager = RecipientManager()

    def init_ui(self):
        self.setupUi(self)
        self.listWidgetContacts.itemClicked.connect(self.redirect_to_chat)

    def get_contacts_for_api(self):
        contacts = requests.get('http://127.0.0.1:8000/api/users/list/')
        for contact in contacts.json():
            item = QListWidgetItem(contact["username"])
            self.listWidgetContacts.addItem(item)

    def redirect_to_chat(self, item):
        self.manager.save_token(item.text())
        print(item.text())
        print(self.manager.get_username_sync())
        self.close()
        self.chat_window = ChatWindow()
        self.chat_window.show()

