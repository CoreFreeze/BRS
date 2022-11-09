from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (QAction, QCheckBox, QComboBox, QDialog,
                               QGridLayout, QGroupBox, QHBoxLayout, QLabel,
                               QLineEdit, QMenu, QMessageBox, QPushButton,
                               QSpinBox, QStyle, QSystemTrayIcon, QTextEdit,
                               QVBoxLayout)


class SystemTray(QDialog):
    def __init__(self, parent) -> None:
        super(SystemTray, self).__init__(parent)

        self.trayIcon = QSystemTrayIcon()
        self.trayIconMenu = QMenu()

        self.restoreAction = QAction()
        self.quitAction = QAction()

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
        self.trayIcon.setContextMenu(self.trayIconMenu)
