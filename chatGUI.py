from chatEmitter import *
import sys
from ui_ui_brs import *
from styleHandler import *
from pysideExtention import *
from settingsHandler import *
from chatServerSocket import *
import socket
import ui_casterName
import ui_closeWindow
import datetime
import threading

PORT = 9090

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadStyle(self, self.ui)
        self.ui.IPLabel.setText(socket.gethostbyname(socket.gethostname()))
        self.readyDisplay = [self.ui.anaReady, self.ui.situRoomA, self.ui.situRoomB]
        self.startServer()
        self.ui.sendButton.clicked.connect(lambda: self.setMessage())
        self.ui.lineEdit.returnPressed.connect(lambda: self.setMessage())
        self.show()

    def startServer(self): 
        chatTCPHandler.casterList = loadCaster()
        chatTCPHandler.ui = self
        bridge = setMessageSig()
        self.chat = ThreadedTCPServer((socket.gethostbyname(socket.gethostname()), PORT), chatTCPHandler)
        
        self.chat.bridge = bridge
        bridge.messageSig.connect(self.showMessage)
        bridge.setReadySig.connect(self.setReady)
        bridge.setNameSig.connect(self.setName)
        thread = threading.Thread(target=self.chat.serve_forever)
        thread.start()

    def setMessage(self):
        message = self.ui.lineEdit.text()
        now = datetime.datetime.now()
        sendMessage = now.strftime("[%H:%M:%S]") + ' 주조' + ' : ' + message
        self.ui.lineEdit.clear()
        self.chat.broadcast(sendMessage)
        self.showMessage(sendMessage)

    @Slot(str)
    def showMessage(self, message):
        self.ui.textBrowser.appendPlainText(message)

    @Slot(int, bool)
    def setReady(self, location, value):
        if value == True:
            self.readyDisplay[location].setStyleSheet("background-color: #00ff40;" "border-right-color: white;" "border-bottom-color: white;" "border-left-color: transparent;" "border-top-color: transparent;" "color: black;")
        elif value == False:
            self.readyDisplay[location].setStyleSheet("background-color: #13151a;" "border-right-color: transparent;" "border-bottom-color: transparent;" "border-left-color: white;" "border-top-color: white;")
        
    @Slot(int, str)
    def setName(self, location, name):
        self.readyDisplay[location].setText(name)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F2:
            casterWindow = casterNameList()
            casterWindow.exec()

    def closeEvent(self, e):
        closeWindow = closeDialog()
        ok = closeWindow.exec()
        if ok == 1:
            self.chat.shutdown()
            e.accept()
        else:
            e.ignore()

    def setAlwaysOnTop(self, value):
        if value == True:
            self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
            self.show()
        else:
            self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, False)
            self.show()

class closeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui_closeWindow.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

class casterNameList(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui_casterName.Ui_Dialog()
        self.ui.setupUi(self)
        self.casterLabel = [self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.lineEdit_4, \
            self.ui.lineEdit_5, self.ui.lineEdit_6, self.ui.lineEdit_7, self.ui.lineEdit_8, self.ui.lineEdit_9, \
                self.ui.lineEdit_10, self.ui.lineEdit_11, self.ui.lineEdit_12 ]
        casterList = loadCaster()
        for index, caster in enumerate(casterList):
            self.casterLabel[index].setText(caster)
        self.show()

    def saveCasterNameList(self):
        casterList = []
        for caster in self.casterLabel:
            casterList.append(caster.text())
        saveCaster(casterList)

    def accept(self):
        self.saveCasterNameList()
        chatTCPHandler.running = False
        super().accept()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())