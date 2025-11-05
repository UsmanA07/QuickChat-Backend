import requests
from PyQt6.QtWidgets import QWidget
import asyncio
from centrifuge import *

from designers.login import Ui_LoginForm
from designers.register import Ui_RegisterForm
from frontend.services.contacts import ContactSelectorWindow
from frontend.config import UserTokenManager


class ClientEventLoggerHandler(ClientEventHandler):

    async def on_connecting(self, ctx: ConnectingContext) -> None:
        print("connecting: %s", ctx)

    async def on_connected(self, ctx: ConnectedContext) -> None:
        print("connected: %s", ctx)

    async def on_disconnected(self, ctx: DisconnectedContext) -> None:
        print("disconnected: %s", ctx)

    async def on_error(self, ctx: ErrorContext) -> None:
        print("client error: %s", ctx)

    async def on_subscribed(self, ctx: ServerSubscribedContext) -> None:
        print("subscribed server-side sub: %s", ctx.data)

    async def on_subscribing(self, ctx: ServerSubscribingContext) -> None:
        print("subscribing server-side sub: %s", ctx.channel)

    async def on_unsubscribed(self, ctx: ServerUnsubscribedContext) -> None:
        print("unsubscribed from server-side sub: %s", ctx.channel)

    async def on_publication(self, ctx: ServerPublicationContext) -> None:
        print("publication from server-side sub: %s", ctx.pub.data)

    async def on_join(self, ctx: ServerJoinContext) -> None:
        print("join in server-side sub: %s", ctx)

    async def on_leave(self, ctx: ServerLeaveContext) -> None:
        print("leave in server-side sub: %s", ctx)


class SubscriptionEventLoggerHandler(SubscriptionEventHandler):

    async def on_subscribing(self, ctx: SubscribingContext) -> None:
        print("subscribing: %s", ctx)

    async def on_subscribed(self, ctx: SubscribedContext) -> None:
        print("subscribed: %s", ctx)

    async def on_unsubscribed(self, ctx: UnsubscribedContext) -> None:
        print("unsubscribed: %s", ctx)

    async def on_publication(self, ctx: PublicationContext) -> None:
        print("publication: %s", ctx.pub.data)

    async def on_join(self, ctx: JoinContext) -> None:
        print("join: %s", ctx)

    async def on_leave(self, ctx: LeaveContext) -> None:
        print("leave: %s", ctx)

    async def on_error(self, ctx: SubscriptionErrorContext) -> None:
        print("subscription error: %s", ctx)


class LoginForm(QWidget, Ui_LoginForm):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.manager = UserTokenManager()

    def init_ui(self):
        self.setupUi(self)
        self.pushButtonLogin.clicked.connect(self.user_login)
        self.pushButtonRegister.clicked.connect(self.redirect_to_register_form)

    def user_login(self):
        username_line = self.lineEditLogin.text()
        password_line = self.lineEditPassword.text()
        data = {
            'username': username_line,
            'password': password_line
        }
        response = requests.post('http://127.0.0.1:8000/api/token/', data=data)
        if 'access' in response.text and 'refresh' in response.text:
            self.subscribe_to_self(username_line)
            self.redirect_to_contacts_form()
            print(response.json()['access'])
            self.manager.save_token(response.json()['access'])
            print(type(self.manager.get_token_sync()))
            print(self.manager.get_token_sync())

    def redirect_to_register_form(self):
        self.close()
        self.register_form = RegisterForm()
        self.register_form.show()

    def redirect_to_contacts_form(self):
        self.close()
        self.contacts_form = ContactSelectorWindow()
        self.contacts_form.show()

    def subscribe_to_self(self, username):
        client = Client(
            "ws://127.0.0.1:8001/connection/websocket",
            events=ClientEventLoggerHandler(),
            get_token=self.manager.get_token,
            use_protobuf=False,
        )
        sub = client.new_subscription(
            channel=f'user_{username}',
            events=SubscriptionEventLoggerHandler(),
            # get_token=get_subscription_token,
        )

        async def main():
            await sub.subscribe()
            await client.connect()
            # await sub.presence(1111)
            print(sub.state)
            print(sub.channel)

        asyncio.run(main())


class RegisterForm(QWidget, Ui_RegisterForm):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButtonRegister.clicked.connect(self.user_register)
        self.pushButtonLogin.clicked.connect(self.redirect_to_login_form)

    def user_register(self):
        username_form = self.lineEditUsername.text()
        email_form = self.lineEditEmail.text()
        password_form = self.lineEditPassword.text()
        data = {
            'username': username_form,
            'email': email_form,
            'password': password_form
        }

        token = requests.post('http://127.0.0.1:8000/api/register/', data=data)
        # if 'blank' not in token.text:
        #     self.redirect_to_login_form()
        print(token.text)

    def redirect_to_login_form(self):
        self.close()
        self.login_form = LoginForm()
        self.login_form.show()
