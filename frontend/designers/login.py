from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(320, 240)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditLogin = QtWidgets.QLineEdit(parent=LoginForm)
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.verticalLayout.addWidget(self.lineEditLogin)
        self.lineEditPassword = QtWidgets.QLineEdit(parent=LoginForm)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.pushButtonLogin = QtWidgets.QPushButton(parent=LoginForm)
        self.pushButtonLogin.setStyleSheet("\n"
"       QPushButton {\n"
"        background-color: #4CAF50;\n"
"        color: white;\n"
"        border: none;\n"
"        padding: 10px;\n"
"        font-size: 14px;\n"
"       }\n"
"       QPushButton:hover {\n"
"        background-color: #45a049;\n"
"       }\n"
"      ")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.verticalLayout.addWidget(self.pushButtonLogin)
        self.pushButtonRegister = QtWidgets.QPushButton(parent=LoginForm)
        self.pushButtonRegister.setStyleSheet("\n"
"       QPushButton {\n"
"        background-color: transparent;\n"
"        color: blue;\n"
"        border: none;\n"
"        text-decoration: underline;\n"
"        font-size: 12px;\n"
"        padding: 5px;\n"
"       }\n"
"       QPushButton:hover {\n"
"        color: darkblue;\n"
"       }\n"
"      ")
        self.pushButtonRegister.setObjectName("pushButtonRegister")
        self.verticalLayout.addWidget(self.pushButtonRegister)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Вход в систему"))
        self.lineEditLogin.setPlaceholderText(_translate("LoginForm", "Введите логин"))
        self.lineEditPassword.setPlaceholderText(_translate("LoginForm", "Введите пароль"))
        self.pushButtonLogin.setText(_translate("LoginForm", "Войти"))
        self.pushButtonRegister.setText(_translate("LoginForm", "Нет аккаунта? Зарегистрируйтесь"))
