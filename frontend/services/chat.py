import asyncio
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtCore import QThread, pyqtSignal, QTimer, Qt
from centrifuge import Client, PublicationContext, SubscriptionEventHandler
from services.config import RecipientManager, TokenManager, UsernameManager
from frontend.designers.chat import Ui_ChatWindow
import requests


class CentrifugeChatWorker(QThread):
    message_received = pyqtSignal(dict)
    status_changed = pyqtSignal(str)
    error_occurred = pyqtSignal(str)

    def __init__(self, token_manager, sort_username):
        super().__init__()
        self.token_manager = token_manager
        self.sort_username = sort_username
        self._should_stop = False

    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self._run_async())
        except Exception as e:
            self.error_occurred.emit(str(e))

    async def _run_async(self):
        try:
            client = Client(
                "ws://127.0.0.1:8001/connection/websocket",
                get_token=self.token_manager.get_token,
                use_protobuf=False,
            )

            subscription = client.new_subscription(
                channel=f'chat:{self.sort_username}',
                events=CentrifugeEventHandler(self.message_received)
            )

            await client.connect()
            self.status_changed.emit("Connected")

            await subscription.subscribe()
            self.status_changed.emit("Subscribed")

            try:
                history = await subscription.history(limit=300)
                for pub in getattr(history, 'publications', []):
                    if hasattr(pub, 'data'):
                        self.message_received.emit(pub.data)
            except Exception:
                pass

            while not self._should_stop:
                await asyncio.sleep(0.1)

        except Exception as e:
            self.error_occurred.emit(str(e))
        finally:
            self.status_changed.emit("Disconnected")

    def stop(self):
        self._should_stop = True


class CentrifugeEventHandler(SubscriptionEventHandler):
    def __init__(self, message_signal):
        super().__init__()
        self.message_signal = message_signal

    async def on_publication(self, ctx: PublicationContext):
        if hasattr(ctx.pub, 'data'):
            self.message_signal.emit(ctx.pub.data)


class ChatWindow(QWidget, Ui_ChatWindow):
    def __init__(self):
        super().__init__()
        self.recipient_manager = RecipientManager()
        self.token_manager = TokenManager()
        self.username_manager = UsernameManager()
        self.worker = None
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.pushButtonSend.clicked.connect(self.send_message)
        self.lineEditMessage.returnPressed.connect(self.send_message)
        self.setup_chat_connection()
        self.update_chat_ui()

    def update_chat_ui(self):
        recipient = self.recipient_manager.get_username_sync()
        self.setWindowTitle(f"Chat with {recipient}")
        self.labelContactName.setText(f"Чат с {recipient}")

    def display_message(self, data):
        sender = data.get('sender', 'Unknown')
        text = data.get('message', '')
        current_user = self.username_manager.get_username_sync()
        own = sender == current_user

        message = QLabel(f"{sender}: {text}")
        message.setWordWrap(True)
        message.setMaximumWidth(500)
        message.setStyleSheet(f"""
            QLabel {{
                background-color: {'#3498db' if own else '#ecf0f1'};
                color: {'white' if own else 'black'};
                padding: 10px;
                border-radius: 8px;
                margin: 2px;
            }}
        """)
        message.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        if own:
            layout.addStretch()
            layout.addWidget(message)
        else:
            layout.addWidget(message)
            layout.addStretch()

        container = QWidget()
        container.setLayout(layout)
        self.verticalLayoutMessages.insertWidget(self.verticalLayoutMessages.count() - 1, container)

        QTimer.singleShot(100, self.scroll_to_bottom)

    def scroll_to_bottom(self):
        scrollbar = self.scrollArea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def sort_username(self):
        return '_'.join(sorted([self.recipient_manager.get_username_sync(), self.username_manager.get_username_sync()]))

    def setup_chat_connection(self):
        self.worker = CentrifugeChatWorker(self.token_manager, self.sort_username())
        self.worker.message_received.connect(self.display_message)
        self.worker.start()

    def send_message(self):
        text = self.lineEditMessage.text().strip()
        if not text:
            return

        recipient = self.recipient_manager.get_username_sync()
        sender = self.username_manager.get_username_sync()

        headers = {'Authorization': f'Bearer {self.token_manager.get_token_sync()}'}
        data = {'recipient': recipient, 'sender': sender, 'message': text}

        try:
            response = requests.post('http://127.0.0.1:8000/api/chat/', headers=headers, data=data)
            if response.status_code == 200:
                self.lineEditMessage.clear()
        except Exception as e:
            print(f'Send error: {e}')

    def closeEvent(self, event):
        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.worker.wait(1000)
        super().closeEvent(event)