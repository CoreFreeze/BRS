from tokenize import String
from PySide2.QtCore import QObject, Signal

class setConnectErrorSig(QObject):
    connectError = Signal()

class setMessageSig(QObject):
    messageSig = Signal(str)
    setReadySig = Signal(int, bool)
    setNameSig = Signal(int, str)
    setBasicSig = Signal(str)
    setSuspendSig = Signal()