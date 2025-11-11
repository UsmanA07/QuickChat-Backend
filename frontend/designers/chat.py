# from PyQt6 import QtCore, QtGui, QtWidgets
#
#
# class Ui_ChatWindow(object):
#     def setupUi(self, ChatWindow):
#         ChatWindow.setObjectName("ChatWindow")
#         ChatWindow.resize(500, 600)
#         self.verticalLayout = QtWidgets.QVBoxLayout(ChatWindow)
#         self.verticalLayout.setContentsMargins(15, 15, 15, 15)
#         self.verticalLayout.setSpacing(10)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.labelContactName = QtWidgets.QLabel(parent=ChatWindow)
#         self.labelContactName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.labelContactName.setStyleSheet("\n"
#                                             "       QLabel {\n"
#                                             "        font-size: 16px;\n"
#                                             "        font-weight: bold;\n"
#                                             "        color: #2c3e50;\n"
#                                             "        padding: 8px;\n"
#                                             "        background-color: #ecf0f1;\n"
#                                             "        border-radius: 4px;\n"
#                                             "       }\n"
#                                             "      ")
#         self.labelContactName.setObjectName("labelContactName")
#         self.verticalLayout.addWidget(self.labelContactName)
#         self.scrollArea = QtWidgets.QScrollArea(parent=ChatWindow)
#         self.scrollArea.setWidgetResizable(True)
#         self.scrollArea.setObjectName("scrollArea")
#         self.scrollAreaWidgetContents = QtWidgets.QWidget()
#         self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 470, 400))
#         self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
#         self.verticalLayoutMessages = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
#         self.verticalLayoutMessages.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayoutMessages.setSpacing(8)
#         self.verticalLayoutMessages.setObjectName("verticalLayoutMessages")
#         self.scrollArea.setWidget(self.scrollAreaWidgetContents)
#         self.verticalLayout.addWidget(self.scrollArea)
#         self.horizontalLayoutInput = QtWidgets.QHBoxLayout()
#         self.horizontalLayoutInput.setObjectName("horizontalLayoutInput")
#         self.lineEditMessage = QtWidgets.QLineEdit(parent=ChatWindow)
#         self.lineEditMessage.setStyleSheet("\n"
#                                            "         QLineEdit {\n"
#                                            "          padding: 10px;\n"
#                                            "          border: 1px solid #bdc3c7;\n"
#                                            "          border-radius: 4px;\n"
#                                            "          font-size: 14px;\n"
#                                            "         }\n"
#                                            "        ")
#         self.lineEditMessage.setObjectName("lineEditMessage")
#         self.horizontalLayoutInput.addWidget(self.lineEditMessage)
#         self.pushButtonSend = QtWidgets.QPushButton(parent=ChatWindow)
#         self.pushButtonSend.setStyleSheet("\n"
#                                           "         QPushButton {\n"
#                                           "          background-color: #3498db;\n"
#                                           "          color: white;\n"
#                                           "          border: none;\n"
#                                           "          padding: 10px 20px;\n"
#                                           "          font-size: 14px;\n"
#                                           "          border-radius: 4px;\n"
#                                           "         }\n"
#                                           "         QPushButton:hover {\n"
#                                           "          background-color: #2980b9;\n"
#                                           "         }\n"
#                                           "        ")
#         self.pushButtonSend.setObjectName("pushButtonSend")
#         self.horizontalLayoutInput.addWidget(self.pushButtonSend)
#         self.verticalLayout.addLayout(self.horizontalLayoutInput)
#
#         self.retranslateUi(ChatWindow)
#         QtCore.QMetaObject.connectSlotsByName(ChatWindow)
#
#     def retranslateUi(self, ChatWindow):
#         _translate = QtCore.QCoreApplication.translate
#         ChatWindow.setWindowTitle(_translate("ChatWindow", "Чат"))
#         self.labelContactName.setText(_translate("ChatWindow", "Имя собеседника"))
#         self.lineEditMessage.setPlaceholderText(_translate("ChatWindow", "Введите сообщение..."))
#         self.pushButtonSend.setText(_translate("ChatWindow", "Отправить"))


from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_ChatWindow(object):
    def setupUi(self, ChatWindow):
        ChatWindow.setObjectName("ChatWindow")
        ChatWindow.resize(500, 600)
        ChatWindow.setMinimumSize(400, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChatWindow)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelContactName = QtWidgets.QLabel(parent=ChatWindow)
        self.labelContactName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelContactName.setStyleSheet("\n"
"       QLabel {\n"
"        font-size: 16px;\n"
"        font-weight: bold;\n"
"        color: #2c3e50;\n"
"        padding: 8px;\n"
"        background-color: #ecf0f1;\n"
"        border-radius: 4px;\n"
"       }\n"
"      ")
        self.labelContactName.setObjectName("labelContactName")
        self.verticalLayout.addWidget(self.labelContactName)
        self.scrollArea = QtWidgets.QScrollArea(parent=ChatWindow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 470, 400))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutMessages = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayoutMessages.setContentsMargins(10, 10, 10, 10)
        self.verticalLayoutMessages.setSpacing(8)
        self.verticalLayoutMessages.setObjectName("verticalLayoutMessages")
        self.verticalLayoutMessages.addStretch(1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayoutInput = QtWidgets.QHBoxLayout()
        self.horizontalLayoutInput.setObjectName("horizontalLayoutInput")
        self.lineEditMessage = QtWidgets.QLineEdit(parent=ChatWindow)
        self.lineEditMessage.setStyleSheet("\n"
"         QLineEdit {\n"
"          padding: 10px;\n"
"          border: 1px solid #bdc3c7;\n"
"          border-radius: 4px;\n"
"          font-size: 14px;\n"
"         }\n"
"        ")
        self.lineEditMessage.setObjectName("lineEditMessage")
        self.horizontalLayoutInput.addWidget(self.lineEditMessage)
        self.pushButtonSend = QtWidgets.QPushButton(parent=ChatWindow)
        self.pushButtonSend.setStyleSheet("\n"
"         QPushButton {\n"
"          background-color: #3498db;\n"
"          color: white;\n"
"          border: none;\n"
"          padding: 10px 20px;\n"
"          font-size: 14px;\n"
"          border-radius: 4px;\n"
"         }\n"
"         QPushButton:hover {\n"
"          background-color: #2980b9;\n"
"         }\n"
"        ")
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.horizontalLayoutInput.addWidget(self.pushButtonSend)
        self.verticalLayout.addLayout(self.horizontalLayoutInput)

        self.retranslateUi(ChatWindow)
        QtCore.QMetaObject.connectSlotsByName(ChatWindow)

    def retranslateUi(self, ChatWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatWindow.setWindowTitle(_translate("ChatWindow", "Чат"))
        self.labelContactName.setText(_translate("ChatWindow", "Имя собеседника"))
        self.lineEditMessage.setPlaceholderText(_translate("ChatWindow", "Введите сообщение..."))
        self.pushButtonSend.setText(_translate("ChatWindow", "Отправить"))