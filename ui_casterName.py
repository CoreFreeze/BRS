# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'casterNameyohIoC.ui'
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
        Dialog.resize(586, 344)
        Dialog.setStyleSheet(u"#Dialog {\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#label, #label_2 {\n"
"	color: #FFFFFF\n"
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

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.portNumber = QLineEdit(self.frame)
        self.portNumber.setObjectName(u"portNumber")
        self.portNumber.setMaximumSize(QSize(250, 16777215))
        self.portNumber.setFont(font)

        self.horizontalLayout_2.addWidget(self.portNumber)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.position = QLineEdit(self.frame)
        self.position.setObjectName(u"position")
        self.position.setMaximumSize(QSize(250, 16777215))
        self.position.setFont(font)

        self.horizontalLayout.addWidget(self.position)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.LocationList = QListWidget(self.frame)
        self.LocationList.setObjectName(u"LocationList")

        self.verticalLayout_2.addWidget(self.LocationList)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.inputLocation = QLineEdit(self.frame)
        self.inputLocation.setObjectName(u"inputLocation")

        self.horizontalLayout_3.addWidget(self.inputLocation)

        self.addLocation = QPushButton(self.frame)
        self.addLocation.setObjectName(u"addLocation")
        self.addLocation.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.addLocation)

        self.delLocation = QPushButton(self.frame)
        self.delLocation.setObjectName(u"delLocation")

        self.horizontalLayout_3.addWidget(self.delLocation)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.addLocation.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Caster Name List", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"PORT", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\uc11c\ubc84 \uc704\uce58", None))
        self.addLocation.setText(QCoreApplication.translate("Dialog", u"\uc785\ub825", None))
        self.delLocation.setText(QCoreApplication.translate("Dialog", u"\uc0ad\uc81c", None))
    # retranslateUi

