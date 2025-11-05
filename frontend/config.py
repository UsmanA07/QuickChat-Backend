from PyQt6.QtCore import QSettings


class UserTokenManager:
    def __init__(self):
        self.settings = QSettings("app", "chat1")

    def save_token(self, token):
        self.settings.setValue("token", token)
        # self.settings.setValue("username", username)

    async def get_token(self):
        return self.settings.value("token", None)

    async def get_username(self):
        return self.settings.value("username", None)

    def get_token_sync(self):
        return self.settings.value("token", None)

    def get_username_sync(self):
        return self.settings.value("username", None)

    def delete_token(self):
        self.settings.remove("token")

    def delete_username(self):
        self.settings.remove("username")
