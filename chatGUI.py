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
import logging
import logging.handlers

PORT = 9090
LOG_FILENAME = 'BRS_Chat_Log.out'

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadStyle(self, self.ui)
        self.logger = logging.getLogger('MyLogger')
        self.logger.setLevel(logging.INFO)
        handler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when='midnight', backupCount=30)
        bf = logging.Formatter('{message}', style='{')
        handler.suffix = 'log-%Y%m%d'
        handler.setFormatter(bf)
        self.logger.addHandler(handler)
        self.readyDisplay = [self.ui.anaReady, self.ui.situRoomA, self.ui.situRoomB]
        retData = loadCaster()
        self.startServer(retData[0], int(retData[1]), retData[3])
        self.ui.IPLabel.setText(socket.gethostbyname(socket.gethostname())+':'+str(retData[1]))
        self.ui.label.setText(retData[3][0])
        self.ui.label_5.setText(retData[3][1])
        self.ui.label_7.setText(retData[3][2])
        self.showLocation = retData[2]
        self.ui.sendButton.clicked.connect(self.setMessage)
        self.ui.lineEdit.returnPressed.connect(self.setMessage)
        self.show()

    def startServer(self, casterNameList, portNum, locationList): 
        chatTCPHandler.casterList = casterNameList
        bridge = setMessageSig()
        self.chat = ThreadedTCPServer((socket.gethostbyname(socket.gethostname()), int(portNum)), chatTCPHandler)
        self.chat.setLocationList(locationList)
        self.chat.bridge = bridge
        bridge.messageSig.connect(self.showMessage)
        bridge.setReadySig.connect(self.setReady)
        bridge.setNameSig.connect(self.setName)
        thread = threading.Thread(target=self.chat.serve_forever)
        thread.start()

    def setMessage(self):
        message = self.ui.lineEdit.text()
        now = datetime.datetime.now()
        sendMessage = now.strftime("[%H:%M:%S]") + ' '+ self.showLocation + ' : ' + message
        self.ui.lineEdit.clear()
        self.chat.broadcast(sendMessage)
        self.showMessage(sendMessage)

    @Slot(str)
    def showMessage(self, message):
        self.ui.textBrowser.appendPlainText(message)
        self.logger.info(message)

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
        retData = loadCaster()
        for index, caster in enumerate(retData[0]):
            self.casterLabel[index].setText(caster)
        self.ui.portNumber.setText(str(retData[1]))
        self.ui.position.setText(retData[2])
        self.ui.LocationList.addItems(retData[3])

        self.ui.addLocation.clicked.connect(self.addLocation)
        self.ui.delLocation.clicked.connect(self.delLocation)

        self.show()

    def addLocation(self):
        location = self.ui.inputLocation.text()
        if self.ui.LocationList.count() > 2:
            return
        self.ui.LocationList.addItem(location)
        self.ui.inputLocation.clear()
    
    def delLocation(self):
        self.ui.LocationList.takeItem(self.ui.LocationList.currentRow())
        self.ui.LocationList.setCurrentRow(-1)
    
    def saveCasterNameList(self):
        casterList = []
        for caster in self.casterLabel:
            casterList.append(caster.text())
        locationList = []
        if self.ui.LocationList.count() == 3:
            for _ in range(0,3):
                locationList.append(self.ui.LocationList.takeItem(0).text())
        else:
            retData = loadCaster()
            locationList = retData[3]
        
        saveCaster(casterList, self.ui.portNumber.text(), self.ui.position.text(), locationList)

    def accept(self):
        self.saveCasterNameList()
        chatTCPHandler.running = False
        super().accept()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())