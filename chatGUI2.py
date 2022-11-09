import sys
from ui_brs_chat import *
from styleHandler import *
from pysideExtention import *
from settingsHandler import *
import ui_closeWindow
import ui_ipSettings
from chatClient import *
from chatEmitter import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.runningStatus = True
        loadStyle(self, self.ui)
        Settings = loadSettings()
        try:
            self.ui.locationDisplay.setText(Settings[2])
            self.readyList = Settings[3]
            self.myLocation = self.readyList.index(Settings[2])
            self.ui.label_2.setText(self.readyList[0])
            self.ui.label_3.setText(self.readyList[1])
            self.ui.label_4.setText(self.readyList[2])
        except:
            self.openSettings()
            Settings = loadSettings()
        self.chat = Client(Settings[2], self.myLocation)
        bridge = setConnectErrorSig()
        bridge2 = setMessageSig()
        self.chat.bridge = bridge
        self.chat.bridge2 = bridge2
        bridge.connectError.connect(self.setConnectError)
        bridge2.messageSig.connect(self.showMessage)
        bridge2.setNameSig.connect(self.setName)
        bridge2.setReadySig.connect(self.setReady)
        bridge2.setBasicSig.connect(self.basicSet)
        bridge2.setSuspendSig.connect(self.suspendAll)

        self.chat.connect(Settings[0], int(Settings[1]))
        self.chat.start()
        self.casterReady = [self.ui.anaReady, self.ui.situRoomA, self.ui.situRoomB]
        self.ui.userSelectButton.clicked.connect(self.setCaster)
        self.ui.readyButton.clicked.connect(self.ready)
        self.readyStatus = False
        self.casterStatus = False
        self.ui.sendButton.clicked.connect(self.setMessage)
        self.ui.lineEdit.returnPressed.connect(self.setMessage)

        self.createActions()
        self.createTrayIcon()

        self.trayIcon.messageClicked.connect(self.showNormal)

        self.trayIcon.show()


    def createActions(self):
        self.restoreAction = QAction("Restore", self)
        self.restoreAction.triggered.connect(self.showNormal)
        
        self.quitAction = QAction("Quit", self)
        self.quitAction.triggered.connect(qApp.quit)


    def createTrayIcon(self):
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon(":/icon/chat.ico"))
        self.trayIcon.setContextMenu(self.trayIconMenu)

    @Slot(int, bool)
    def setReady(self, location, value):
        if value is True:
            self.casterReady[location].setStyleSheet("background-color: #00ff40;" "border-right-color: white;" "border-bottom-color: white;" "border-left-color: transparent;" "border-top-color: transparent;" "color: black;")
        elif value is False:
            self.casterReady[location].setStyleSheet("background-color: #13151a;" "border-right-color: transparent;" "border-bottom-color: transparent;" "border-left-color: white;" "border-top-color: white;")

    @Slot(int, str)
    def setName(self, location, name):
        self.casterReady[location].setText(name)

    @Slot(str)
    def basicSet(self, message):
        msg = message.split('&')
        for i in range(0, len(self.casterReady)):
            if i != self.myLocation:
                if msg[((i + 1) * 2) - 1] != '':
                    self.casterReady[i].setText(msg[((i + 1) * 2) - 1])
                    self.setReady(i, msg[(i + 1) * 2]=='True')

        casterList = []
        for i in range(0, int(msg[7])):
            casterList.append(str(msg[i + 8]).strip())
        
        self.setCasters(casterList)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F2:
            self.openSettings()

    def openSettings(self):
        settingsWindow = Settings()
        settingsWindow.exec()

    def setCasters(self, casters):
        self.ui.userSelectBox.addItems(casters)
        self.ui.userSelectBox.setPlaceholderText(' ') 

    def setCaster(self):
        user = self.ui.userSelectBox.currentText()
        if user != ' ' and user is not None:
            self.readyStatus = False
            self.casterStatus = True
            self.ui.userDisplay.setText('현재 사용자는 '+ user + ' 입니다.')
            sendMessage = '1&'+str(self.chat.getLocationIndex())+'&'+user+'&'+str(self.readyStatus)
            self.chat.write(sendMessage)
        else: 
            pass

    @Slot()
    def setConnectError(self):
        if self.runningStatus is False:
            return
        closeWindow = closeDialog()
        closeWindow.ui.label.setText('서버와 연결이 끊어졌습니다.')
        self.ui.textBrowser.appendPlainText('서버와 연결이 끊어졌습니다.')
        closeWindow.exec()

    @Slot()
    def suspendAll(self):
        for i in range(0,3):
            self.setReady(i, False)
        self.readyStatus = False

    def setMessage(self):
        if self.casterStatus is False:
            return
        user = self.ui.userSelectBox.currentText()
        message = self.ui.lineEdit.text()
        sendMessage = '[' + self.ui.lcdNumber.getTime() +'] ' + user + ' : ' + message
        self.ui.lineEdit.clear()
        self.chat.write(sendMessage)

    @Slot(str)
    def showMessage(self, message):
        self.ui.textBrowser.appendPlainText(message)
        QApplication.alert(self)
        splitedMessage = message.split()
        if len(splitedMessage) == 4:
            if splitedMessage[1] != self.ui.userSelectBox.currentText():
                self.trayIcon.showMessage(
                        splitedMessage[1],
                        splitedMessage[3],
                        QSystemTrayIcon.NoIcon,
                        100,
                )


    def ready(self):
        if self.casterStatus is False:
            return
        self.readyStatus = not self.readyStatus
        user = self.ui.userSelectBox.currentText()
        if user != ' ' and user is not None:
            sendMessage = '1&'+str(self.chat.getLocationIndex())+'&'+user+'&'+str(self.readyStatus)
            self.chat.write(sendMessage)
        else: 
            pass

    def closeEvent(self, e):
        closeWindow = closeDialog()
        ok = closeWindow.exec()
        if ok == 1:
            self.runningStatus = False
            if hasattr(self, 'chat'):
                self.chat.stop()
            e.accept()
        else:
            e.ignore()

class closeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui_closeWindow.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

class Settings(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui_ipSettings.Ui_Dialog()
        self.ui.setupUi(self)
        Settings = loadSettings()
        self.ui.lineEdit.setText(Settings[0])
        self.ui.lineEdit_2.setText(str(Settings[1]))
        self.ui.LocationList.addItems(Settings[3])
        self.changeLocationBoxList(Settings[2])

        self.ui.addLocation.clicked.connect(self.addLocation)
        self.ui.delLocation.clicked.connect(self.delLocation)

        self.show()

    def addLocation(self):
        location = self.ui.inputLocation.text()
        if self.ui.LocationList.count() > 2:
            return
        self.ui.LocationList.addItem(location)
        self.ui.inputLocation.clear()

        self.changeLocationBoxList()
    
    def delLocation(self):
        self.ui.LocationList.takeItem(self.ui.LocationList.currentRow())
        self.ui.LocationList.setCurrentRow(-1)

    def changeLocationBoxList(self, location = None):
        locations = []
        for index in range(0, self.ui.LocationList.count()):
            locations.append(self.ui.LocationList.item(index).text())
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(locations)
        try:
            self.ui.comboBox.setCurrentIndex(locations.index(location))
        except:
            self.ui.comboBox.setCurrentIndex(-1)

    def saveSettings(self):
        locationList = []
        if self.ui.LocationList.count() == 3:
            for _ in range(0,3):
                locationList.append(self.ui.LocationList.takeItem(0).text())
        else:
            retData = loadSettings()
            locationList = retData[3]
        saveSettings(self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), self.ui.comboBox.currentText(), locationList)

    def accept(self):
        self.saveSettings()
        super().accept()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    #window.chatStart()

    sys.exit(app.exec_())