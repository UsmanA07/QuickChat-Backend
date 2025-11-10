from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHBoxLayout, QWidget


class Ui_ContactSelector(object):
    def setupUi(self, ContactSelector):
        ContactSelector.setObjectName("ContactSelector")
        ContactSelector.resize(400, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(ContactSelector)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidgetContacts = QtWidgets.QListWidget(parent=ContactSelector)
        self.listWidgetContacts.setAlternatingRowColors(True)
        self.listWidgetContacts.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.listWidgetContacts.setObjectName("listWidgetContacts")
        self.verticalLayout.addWidget(self.listWidgetContacts)
        self.horizontalLayoutButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutButtons.setObjectName("horizontalLayoutButtons")
        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.addStretch()
        self.verticalLayout.addWidget(button_container)

        self.retranslateUi(ContactSelector)
        QtCore.QMetaObject.connectSlotsByName(ContactSelector)

    def retranslateUi(self, ContactSelector):
        _translate = QtCore.QCoreApplication.translate
        ContactSelector.setWindowTitle(_translate("ContactSelector", "Выбор контакта"))
