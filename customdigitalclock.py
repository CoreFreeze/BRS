from PySide2 import QtWidgets
from PySide2 import QtCore

class customDigitalClock(QtWidgets.QLCDNumber):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.showTime()
        timer = QtCore.QTimer(self)
        timer.setInterval(1000)
        timer.timeout.connect(self.showTime)
        timer.start()

    def getTime(self):
        return self.text

    def showTime(self):
        time = QtCore.QTime.currentTime()
        self.text = time.toString("hh:mm:ss")
        self.display(self.text)