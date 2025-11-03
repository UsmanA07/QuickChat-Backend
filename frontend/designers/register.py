from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RegisterForm(object):
    def setupUi(self, RegisterForm):
        RegisterForm.setObjectName("RegisterForm")
        RegisterForm.resize(360, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(RegisterForm)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelUsername = QtWidgets.QLabel(parent=RegisterForm)
        self.labelUsername.setObjectName("labelUsername")
        self.verticalLayout.addWidget(self.labelUsername)
        self.lineEditUsername = QtWidgets.QLineEdit(parent=RegisterForm)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.verticalLayout.addWidget(self.lineEditUsername)
        self.labelEmail = QtWidgets.QLabel(parent=RegisterForm)
        self.labelEmail.setObjectName("labelEmail")
        self.verticalLayout.addWidget(self.labelEmail)
        self.lineEditEmail = QtWidgets.QLineEdit(parent=RegisterForm)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.verticalLayout.addWidget(self.lineEditEmail)
        self.labelPassword = QtWidgets.QLabel(parent=RegisterForm)
        self.labelPassword.setObjectName("labelPassword")
        self.verticalLayout.addWidget(self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(parent=RegisterForm)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.pushButtonRegister = QtWidgets.QPushButton(parent=RegisterForm)
        self.pushButtonRegister.setStyleSheet("\n"
"       QPushButton {\n"
"        background-color: #2196F3;\n"
"        color: white;\n"
"        border: none;\n"
"        padding: 12px;\n"
"        font-size: 14px;\n"
"        border-radius: 4px;\n"
"       }\n"
"       QPushButton:hover {\n"
"        background-color: #1976D2;\n"
"       }\n"
"      ")
        self.pushButtonRegister.setObjectName("pushButtonRegister")
        self.verticalLayout.addWidget(self.pushButtonRegister)
        self.pushButtonLogin = QtWidgets.QPushButton(parent=RegisterForm)
        self.pushButtonLogin.setStyleSheet("\n"
"       QPushButton {\n"
"        background-color: transparent;\n"
"        color: #2196F3;\n"
"        border: none;\n"
"        text-decoration: underline;\n"
"        font-size: 12px;\n"
"        padding: 8px;\n"
"       }\n"
"       QPushButton:hover {\n"
"        color: #1976D2;\n"
"       }\n"
"      ")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.verticalLayout.addWidget(self.pushButtonLogin, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.retranslateUi(RegisterForm)
        QtCore.QMetaObject.connectSlotsByName(RegisterForm)

    def retranslateUi(self, RegisterForm):
        _translate = QtCore.QCoreApplication.translate
        RegisterForm.setWindowTitle(_translate("RegisterForm", "Регистрация"))
        self.labelUsername.setText(_translate("RegisterForm", "Логин:"))
        self.lineEditUsername.setPlaceholderText(_translate("RegisterForm", "Введите логин"))
        self.labelEmail.setText(_translate("RegisterForm", "Email:"))
        self.lineEditEmail.setPlaceholderText(_translate("RegisterForm", "Введите email"))
        self.labelPassword.setText(_translate("RegisterForm", "Пароль:"))
        self.lineEditPassword.setPlaceholderText(_translate("RegisterForm", "Введите пароль"))
        self.pushButtonRegister.setText(_translate("RegisterForm", "Зарегистрироваться"))
        self.pushButtonLogin.setText(_translate("RegisterForm", "Уже есть аккаунт? Войти"))
