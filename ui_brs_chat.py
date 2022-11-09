# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'brs_chatudnnPe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from customdigitalclock import customDigitalClock

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(492, 664)
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
"#frame_2 {\n"
"	border-radius:20px;\n"
"	background-color: #1f232a;\n"
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
"}\n"
"#userSelectBox {\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"#locationDisplay {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"#userSelectButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"#readyButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 5px;\n"
""
                        "	background-color: rgb(161, 161, 179);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#sendButton {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"#userDisplay {\n"
"	border: 1px solid;\n"
"	border-color: white;\n"
"	border-radius: 5px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.locationDisplay = QLabel(self.frame)
        self.locationDisplay.setObjectName(u"locationDisplay")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.locationDisplay.setFont(font)
        self.locationDisplay.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.locationDisplay)

        self.userSelectBox = QComboBox(self.frame)
        self.userSelectBox.setObjectName(u"userSelectBox")
        font1 = QFont()
        font1.setPointSize(20)
        self.userSelectBox.setFont(font1)

        self.horizontalLayout_4.addWidget(self.userSelectBox)

        self.userSelectButton = QPushButton(self.frame)
        self.userSelectButton.setObjectName(u"userSelectButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userSelectButton.sizePolicy().hasHeightForWidth())
        self.userSelectButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(15)
        self.userSelectButton.setFont(font2)

        self.horizontalLayout_4.addWidget(self.userSelectButton)


        self.verticalLayout_6.addWidget(self.frame)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.userDisplay = QLabel(self.frame_2)
        self.userDisplay.setObjectName(u"userDisplay")
        self.userDisplay.setFont(font1)
        self.userDisplay.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.userDisplay)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_6.addWidget(self.widget)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.widget_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber = customDigitalClock(self.frame_7)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setPointSize(25)
        self.lcdNumber.setFont(font3)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_8.addWidget(self.lcdNumber)


        self.verticalLayout_7.addWidget(self.frame_7)


        self.verticalLayout_6.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(4)
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.widget_3)
        self.frame_3.setObjectName(u"frame_3")
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.frame_3.setFont(font4)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color: rgb(62, 209, 36);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignTop)

        self.anaReady = QLabel(self.frame_3)
        self.anaReady.setObjectName(u"anaReady")
        sizePolicy3.setHeightForWidth(self.anaReady.sizePolicy().hasHeightForWidth())
        self.anaReady.setSizePolicy(sizePolicy3)
        self.anaReady.setSizeIncrement(QSize(0, 0))
        self.anaReady.setBaseSize(QSize(0, 0))
        font6 = QFont()
        font6.setPointSize(25)
        font6.setBold(True)
        font6.setWeight(75)
        self.anaReady.setFont(font6)
        self.anaReady.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.anaReady)

        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.widget_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFont(font4)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color: rgb(62, 209, 36);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignTop)

        self.situRoomA = QLabel(self.frame_4)
        self.situRoomA.setObjectName(u"situRoomA")
        sizePolicy3.setHeightForWidth(self.situRoomA.sizePolicy().hasHeightForWidth())
        self.situRoomA.setSizePolicy(sizePolicy3)
        self.situRoomA.setFont(font6)
        self.situRoomA.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.situRoomA)

        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.widget_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFont(font4)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: rgb(62, 209, 36);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignTop)

        self.situRoomB = QLabel(self.frame_5)
        self.situRoomB.setObjectName(u"situRoomB")
        sizePolicy3.setHeightForWidth(self.situRoomB.sizePolicy().hasHeightForWidth())
        self.situRoomB.setSizePolicy(sizePolicy3)
        self.situRoomB.setMinimumSize(QSize(0, 130))
        self.situRoomB.setFont(font6)
        self.situRoomB.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.situRoomB)

        self.verticalLayout_4.setStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy4)
        self.verticalLayout_9 = QVBoxLayout(self.widget_5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.widget_5)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy3.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy3)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.readyButton = QPushButton(self.frame_8)
        self.readyButton.setObjectName(u"readyButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.readyButton.sizePolicy().hasHeightForWidth())
        self.readyButton.setSizePolicy(sizePolicy5)
        self.readyButton.setFont(font3)

        self.verticalLayout_10.addWidget(self.readyButton)


        self.verticalLayout_9.addWidget(self.frame_8)


        self.verticalLayout_6.addWidget(self.widget_5)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(3)
        sizePolicy6.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy6)
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QPlainTextEdit(self.widget_2)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy7)
        self.textBrowser.setMinimumSize(QSize(0, 0))
        self.textBrowser.setFont(font1)
        self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_5.addWidget(self.textBrowser)

        self.frame_6 = QFrame(self.widget_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font1)

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.sendButton = QPushButton(self.frame_6)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setMinimumSize(QSize(100, 0))
        self.sendButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.sendButton)


        self.verticalLayout_5.addWidget(self.frame_6)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.verticalLayout_6.setStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.locationDisplay.setText(QCoreApplication.translate("MainWindow", u"\uc704\uce58", None))
        self.userSelectBox.setCurrentText("")
        self.userSelectButton.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc790 \ubcc0\uacbd", None))
        self.userDisplay.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac \uc0ac\uc6a9\uc790\ub294 OOO\uc785\ub2c8\ub2e4.", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc544\ub098\ubd80\uc2a4", None))
        self.anaReady.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud669\uc2e4A", None))
        self.situRoomA.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud669\uc2e4B", None))
        self.situRoomB.setText("")
        self.readyButton.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"\uc804\uc1a1", None))
    # retranslateUi

