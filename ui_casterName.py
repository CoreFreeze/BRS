# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'casterNameEgiKNA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(392, 280)
        Dialog.setStyleSheet(u"#Dialog {\n"
"	background-color: #1f232a;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(10)
        self.lineEdit_8 = QLineEdit(Dialog)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 2, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 0, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 1, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(Dialog)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 2, 2, 1, 1)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 1, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(Dialog)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 1, 2, 1, 1)

        self.lineEdit_7 = QLineEdit(Dialog)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 2, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(Dialog)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout.addWidget(self.lineEdit_10, 3, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(Dialog)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout.addWidget(self.lineEdit_11, 3, 1, 1, 1)

        self.lineEdit_12 = QLineEdit(Dialog)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout.addWidget(self.lineEdit_12, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Caster Name List", None))
    # retranslateUi

