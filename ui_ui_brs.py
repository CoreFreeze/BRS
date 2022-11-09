# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_brsFApQch.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1109, 566)
        icon = QIcon()
        icon.addFile(u":/icon/chat.ico", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"#anaReady, #situRoomA, #situRoomB {\n"
"	border-radius:20px;\n"
"	border: 1px solid;\n"
"	border-left-color: white;\n"
"	border-top-color: white;\n"
"	background-color: #13151a;\n"
"}\n"
"\n"
"#sendButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"#textBrowser {\n"
"	background-color: #2c313c;\n"
"}\n"
"#frame_6 {\n"
"	background-color: #1f232a;\n"
"}\n"
"#lineEdit {\n"
"	background-color: white;\n"
"	color: black;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setPointSize(40)
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_10)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.IPLabel = QLabel(self.frame_5)
        self.IPLabel.setObjectName(u"IPLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.IPLabel.sizePolicy().hasHeightForWidth())
        self.IPLabel.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(20)
        self.IPLabel.setFont(font1)

        self.horizontalLayout_3.addWidget(self.IPLabel)

        self.onTopCheckBox = QCheckBox(self.frame_5)
        self.onTopCheckBox.setObjectName(u"onTopCheckBox")

        self.horizontalLayout_3.addWidget(self.onTopCheckBox, 0, Qt.AlignRight)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(62, 209, 36);")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.anaReady = QLabel(self.frame_2)
        self.anaReady.setObjectName(u"anaReady")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(5)
        sizePolicy2.setHeightForWidth(self.anaReady.sizePolicy().hasHeightForWidth())
        self.anaReady.setSizePolicy(sizePolicy2)
        self.anaReady.setSizeIncrement(QSize(10, 10))
        self.anaReady.setBaseSize(QSize(100, 100))
        font3 = QFont()
        font3.setPointSize(75)
        font3.setBold(True)
        font3.setWeight(75)
        self.anaReady.setFont(font3)
        self.anaReady.setFrameShape(QFrame.Panel)
        self.anaReady.setFrameShadow(QFrame.Sunken)
        self.anaReady.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.anaReady)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(62, 209, 36);")

        self.verticalLayout_2.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.situRoomA = QLabel(self.frame_3)
        self.situRoomA.setObjectName(u"situRoomA")
        sizePolicy2.setHeightForWidth(self.situRoomA.sizePolicy().hasHeightForWidth())
        self.situRoomA.setSizePolicy(sizePolicy2)
        self.situRoomA.setSizeIncrement(QSize(10, 10))
        self.situRoomA.setBaseSize(QSize(100, 100))
        self.situRoomA.setFont(font3)
        self.situRoomA.setFrameShape(QFrame.Panel)
        self.situRoomA.setFrameShadow(QFrame.Sunken)
        self.situRoomA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.situRoomA)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(62, 209, 36);")

        self.verticalLayout_3.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.situRoomB = QLabel(self.frame_4)
        self.situRoomB.setObjectName(u"situRoomB")
        sizePolicy2.setHeightForWidth(self.situRoomB.sizePolicy().hasHeightForWidth())
        self.situRoomB.setSizePolicy(sizePolicy2)
        self.situRoomB.setFont(font3)
        self.situRoomB.setFrameShape(QFrame.Panel)
        self.situRoomB.setFrameShadow(QFrame.Sunken)
        self.situRoomB.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.situRoomB)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout_5.addWidget(self.frame)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QPlainTextEdit(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFont(font1)
        self.textBrowser.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_7.addWidget(self.textBrowser)

        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.sendButton = QPushButton(self.frame_6)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setMinimumSize(QSize(100, 0))
        self.sendButton.setFont(font1)
        self.sendButton.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.sendButton)


        self.verticalLayout_7.addWidget(self.frame_6)


        self.verticalLayout_5.addWidget(self.widget)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 2)
        self.verticalLayout_5.setStretch(2, 1)

        self.verticalLayout_4.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"BRS", None))
        self.IPLabel.setText(QCoreApplication.translate("MainWindow", u"IP: 000.000.000.000", None))
        self.onTopCheckBox.setText(QCoreApplication.translate("MainWindow", u"\ud56d\uc0c1 \uc704\uc5d0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc544\ub098\ubd80\uc2a4", None))
        self.anaReady.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud669\uc2e4 A", None))
        self.situRoomA.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud669\uc2e4 B", None))
        self.situRoomB.setText("")
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"\uc804\uc1a1", None))
    # retranslateUi

