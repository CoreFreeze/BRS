from pydoc import text
import sys
from ui_ui_brs import *
from styleHandler import *
from pysideExtention import *
from settingsHandler import *
import ui_closeWindow
import ui_ipSettings
from chatClient import *
from chatEmitter import *
import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadStyle(self, self.ui)
        self.runningStatus = True
        Settings = loadSettings()
        self.myLocation = Settings[1]
        self.ui.IPLabel.setText('')

        self.chat = Client(Settings[1])
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
        self.chat.connect(Settings[0], 9090)
        self.chat.start()
        self.casterReady = [self.ui.anaReady, self.ui.situRoomA, self.ui.situRoomB]
        self.ui.sendButton.clicked.connect(lambda: self.setMessage())
        self.ui.lineEdit.returnPressed.connect(lambda: self.setMessage())
        self.ui.onTopCheckBox.toggled.connect(self.setAlwaysOnTop)

    def setAlwaysOnTop(self, value):
        if value == True:
            self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
            self.show()
        else:
            self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, False)
            self.show()

    @Slot(int, bool)
    def setReady(self, location, value):
        if value is True:
            self.casterReady[location].setStyleSheet("background-color: #00ff40;" "border-right-color: white;" "border-bottom-color: white;" "border-left-color: transparent;" "border-top-color: transparent;"  "color: black;")
        elif value is False:
            self.casterReady[location].setStyleSheet("background-color: #13151a;" "border-right-color: transparent;" "border-bottom-color: transparent;" "border-left-color: white;" "border-top-color: white;")

    @Slot(int, str)
    def setName(self, location, name):
        self.casterReady[location].setText(name)

    @Slot(str)
    def basicSet(self, message):
        msg = message.split('&')
        for i in range(0, len(self.casterReady)):
            if msg[((i + 1) * 2) - 1] != '':
                self.casterReady[i].setText(msg[((i + 1) * 2) - 1])
                self.setReady(i, msg[(i + 1) * 2]=='True')

        casterList = []
        for i in range(0, int(msg[7])):
            casterList.append(str(msg[i + 8]).strip())
        

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F2:
            settingsWindow = Settings()
            settingsWindow.exec()

    @Slot()
    def setConnectError(self):
        if self.runningStatus is False:
            return
        closeWindow = closeDialog()
        closeWindow.ui.label.setText('서버와 연결이 끊어졌습니다.')
        self.ui.textBrowser.appendPlainText('서버와 연결이 끊어졌습니다.')
        ok = closeWindow.exec()

    def setCasterLocation(self, index, caster):
        self.setName(index,caster)

    def suspendAll(self):
        for i in range(0,3):
            self.setReady(i, False)
        self.readyStatus = False

    def setMessage(self):
        user = self.myLocation
        message = self.ui.lineEdit.text()
        now = datetime.datetime.now()
        sendMessage = now.strftime("[%H:%M:%S] ") + user + ' : ' + message
        self.ui.lineEdit.clear()
        self.chat.write(sendMessage)

    @Slot(str)
    def showMessage(self, message):
        self.ui.textBrowser.appendPlainText(message)

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
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
        self.show()

class Settings(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui_ipSettings.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
        Settings = loadSettings()
        self.ui.lineEdit.setText(Settings[0])
        locations = ['1부조','2부조','편성제작국','교통정보상황실', 'DJ Room']
        self.ui.comboBox.addItems(locations)
        try:
            self.ui.comboBox.setCurrentIndex(locations.index(Settings[1]))
        except:
            self.ui.comboBox.setCurrentIndex(0)
        self.show()

    def saveSettings(self):
        saveSettings(self.ui.lineEdit.text(), self.ui.comboBox.currentText())

    def accept(self):
        self.saveSettings()
        super().accept()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    #window.chatStart()

    sys.exit(app.exec_())