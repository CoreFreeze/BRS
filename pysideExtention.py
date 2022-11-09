from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import Signal

class QMainWindow(QMainWindow):
    def __init__(self, parent=None, socket=None):
        super().__init__(parent)
        self.socket=socket
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        cursor = QtGui.QCursor()
        xPos = cursor.pos().x()
        yPos = cursor.pos().y()
        if hasattr(self, "floatingWidgets"):
            for x in self.floatingWidgets:
                if hasattr(x, "autoHide") and x.autoHide:
                    x.collapseMenu()

    def updateRestoreButtonIcon(self):
        if self.isMaximized():
            if len(str(self.maximizedIcon)) > 0:
                self.restoreBtn.setIcon(QtGui.QIcon(str(self.maximizedIcon)))
        else:
            if len(str(self.normalIcon)) > 0:
                self.restoreBtn.setIcon(QtGui.QIcon(str(self.normalIcon)))


    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
        self.updateRestoreButtonIcon()

    def moveWindow(self, e):

        if not self.isMaximized():
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()
        else:
            self.showNormal()

    def toggleWindowSize(self, e):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
        self.updateRestoreButtonIcon()
    
    def checkButtonGroup(self):
        btn = self.sender()
        group = btn.group
        # print(self)
        groupBtns = getattr(self, "group_btns_"+str(group))
        active = getattr(self, "group_active_"+str(group))
        notActive = getattr(self, "group_not_active_"+str(group))

        for x in groupBtns:
            if not x == btn:
                x.setStyleSheet(notActive)
                x.active = False

        btn.setStyleSheet(active)
        btn.active = True

    def close(self):
        super().close()

class QPushButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        ########################################################################
        ## CREATE ANIMATION
        ########################################################################
        self._animation = QtCore.QVariantAnimation()
        self._animation.setStartValue(0.00001)
        self._animation.setEndValue(0.9999)
        self._animation.valueChanged.connect(self._animate)
        # self._animation.setEasingCurve(QtCore.QEasingCurve.OutQuad)

        # DEAFAULT ANIMATION DURATION
        self._animation.setDuration(500)

        self._shadowAnimation = QtCore.QVariantAnimation()
        self._shadowAnimation.setStartValue(0)
        self._shadowAnimation.setEndValue(10)
        self._shadowAnimation.valueChanged.connect(self._animateShadow)
        # self._shadowAnimation.setEasingCurve(QtCore.QEasingCurve.OutQuad)

        # DEAFAULT ANIMATION DURATION
        self._shadowAnimation.setDuration(500)

        # DEFAULT COLOR
        self.color1 = None
        self.color2 = None

        # DEFAULT ANIMATION TRIGGER FOR BUTTON IS HOVER EVENT
        self.setObjectAnimatedOn = "hover"

        # DEFAULT ANIMATION TRIGGER FOR BUTTON ICON IS NONE
        self.setIconAnimatedOn = None

        # ANIMATE BORDER AND BACKGROUND BY DEFAULT
        self.setObjectAnimate = "both"

        # SET DEFAULT FALLBACK STYLE TO NINE
        self.fallBackStyle = None

        # SET DEFAULT FALLBACK STYLE TO NONE
        self.defaultStyle = None

        # SET DEFAULT FALLBACK STYLE TO NONE
        self.clickPosition = None

        # SET DEFAULT FALLBACK STYLE TO NONE
        self.mousePosition = None

        # SET DEFAULT SHADOW EVENT TO NONE
        self.applyShadowOn = None

    ########################################################################
    ## BUTTON THEMES
    ########################################################################
    def setObjectTheme(self, theme):
        if str(theme) == "1":
            self.color1 = QtGui.QColor(9, 27, 27, 25)
            self.color2 = QtGui.QColor(85, 255, 255, 255)
        elif str(theme) == "2":
            self.color1 = QtGui.QColor(240, 53, 218)
            self.color2 = QtGui.QColor(61, 217, 245)
        elif str(theme) == "3":
            self.color1 = QtGui.QColor("#C0DB50")
            self.color2 = QtGui.QColor("#100E19")
        elif str(theme) == "4":
            self.color1 = QtGui.QColor("#FF16EB")
            self.color2 = QtGui.QColor("#100E19")
        elif str(theme) == "5":
            self.color1 = QtGui.QColor("#FF4200")
            self.color2 = QtGui.QColor("#100E19")
        elif str(theme) == "6":
            self.color1 = QtGui.QColor("#000046")
            self.color2 = QtGui.QColor("#1CB5E0")
        elif str(theme) == "7":
            self.color1 = QtGui.QColor("#EB5757")
            self.color2 = QtGui.QColor("#000000")
        elif str(theme) == "8":
            self.color1 = QtGui.QColor("#FF8235")
            self.color2 = QtGui.QColor("#30E8BF")
        elif str(theme) == "9":
            self.color1 = QtGui.QColor("#20002c")
            self.color2 = QtGui.QColor("#cbb4d4")
        elif str(theme) == "10":
            self.color1 = QtGui.QColor("#C33764")
            self.color2 = QtGui.QColor("#1D2671")
        elif str(theme) == "11":
            self.color1 = QtGui.QColor("#ee0979")
            self.color2 = QtGui.QColor("#ff6a00")
        elif str(theme) == "12":
            self.color1 = QtGui.QColor("#242424")
            self.color2 = QtGui.QColor("#FA0000")
        elif str(theme) == "13":
            self.color1 = QtGui.QColor("#25395f")
            self.color2 = QtGui.QColor("#55ffff")

        else:
            raise Exception("Unknown theme '" +str(theme)+ "'")



    ########################################################################
    ## SET BUTTON THEME
    ########################################################################
    def setObjectCustomTheme(self, color1, color2):
        self.color1 = QtGui.QColor(color1)
        self.color2 = QtGui.QColor(color2)

    ########################################################################
    ## SET BUTTON ANIMATION
    ########################################################################
    def setObjectAnimation(self, animation):
        self.setObjectAnimate = str(animation)

    ########################################################################
    ## SET BUTTON ANIMATION EVENT TRIGGER
    ########################################################################
    def setObjectAnimateOn(self, trigger):
        self.setObjectAnimatedOn = trigger
        if str(trigger) == "click":
            self._animation.setDuration(200)
        else:
            self._animation.setDuration(500)

    ########################################################################
    ## SET BUTTON STYLESHEET TO BE AOOLIED AFTER ANIMATION IS OVER
    ########################################################################
    def setObjectFallBackStyle(self, style):
        self.fallBackStyle = str(style)

    ########################################################################
    ## SET BUTTON DEFAULT STYLESHEET THAT WILL BE ADDED ALONGSIDE ANIMATION
    ## STYLE
    ########################################################################
    def setObjectDefaultStyle(self, style):
        self.defaultStyle = str(style)

    ########################################################################
    ## SET BUTTON BUTTON HOVER IN EVENT
    ########################################################################
    def enterEvent(self, event):
        self.mousePosition = "over"
        if self.setObjectAnimatedOn  == "hover" or self.setObjectAnimatedOn is None:
            self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
            self._animation.start()
        #
        if self.setIconAnimatedOn == "hover":
            if hasattr(self, 'anim'):
                self.anim.start()
        if self.applyShadowOn == "hover":
            if self.animateShadow:
                self._shadowAnimation.setDirection(QtCore.QAbstractAnimation.Forward)
                self._shadowAnimation.start()

            else:
                self.setGraphicsEffect(self.shadow)

        super().enterEvent(event)

    ########################################################################
    ## SET BUTTON HOVER OUT EVENT
    ########################################################################
    def leaveEvent(self, event):
        self.mousePosition = "out"
        if self.setObjectAnimatedOn  == "hover" or self.setObjectAnimatedOn is None:
            self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
            self._animation.start()
            self._animation.finished.connect(lambda: self.applyDefaultStyle())

        if self.applyShadowOn == "hover":
            if self.animateShadow:
                self._shadowAnimation.setDirection(QtCore.QAbstractAnimation.Backward)
                self._shadowAnimation.start()
                self._shadowAnimation.finished.connect(lambda: self.removeButtonShadow())
                # disconnect(self._shadowAnimation.finished, self.removeButtonShadow())

        super().leaveEvent(event)


    ########################################################################
    ## SET BUTTON MOUSE PRESS 'DOWN' EVENT
    ########################################################################
    def mousePressEvent(self, event):
        self.clickPosition = "down"
        if self.setObjectAnimatedOn  == "click":
            self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
            self._animation.start()
        #
        if self.setIconAnimatedOn == "click":
            if hasattr(self, 'anim'):
                self.anim.start()
        if self.applyShadowOn == "click":
            if self.animateShadow:
                self._shadowAnimation.setDirection(QtCore.QAbstractAnimation.Forward)
                self._shadowAnimation.start()
            else:
                self.setGraphicsEffect(self.shadow)

        super().mousePressEvent(event)

    ########################################################################
    ## SET BUTTON MOUSE PRESS 'UP' EVENT
    ########################################################################
    def mouseReleaseEvent(self, event):
        self.clickPosition = "up"
        if self.setObjectAnimatedOn  == "click":
            self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
            self._animation.start()
            self._animation.finished.connect(lambda: self.applyDefaultStyle())
        if self.applyShadowOn == "click":
            if self.animateShadow:
                self._shadowAnimation.setDirection(QtCore.QAbstractAnimation.Backward)
                self._shadowAnimation.start()
                self._shadowAnimation.finished.connect(lambda: self.removeButtonShadow())
            else:
                self.setGraphicsEffect(self.shadow)
        super().mouseReleaseEvent(event)

    def doNothing(self):
        pass


    ########################################################################
    ## REMOVE BUTTON SHADOW
    ##
    ########################################################################
    def removeButtonShadow(self):
        # self.shadow.setBlurRadius(0)
        #######################################################################
        ## # Appy shadow to button
        ########################################################################
        self.setGraphicsEffect(self.shadow)

    ########################################################################
    ## APPLY BUTTON STYLESHEET AFTER ANIMATION IS OVER
    ## AND STOP ICON ANIMATIONS
    ########################################################################
    def applyDefaultStyle(self):
        # print(self.setIconAnimatedOn, self.clickPosition, self.mousePosition)
        if self.mousePosition == "out" or self.clickPosition == "up":
            if self.fallBackStyle is None:
                pass
            else:
                if self.defaultStyle is not None:
                    self.setStyleSheet(str(self.defaultStyle + self.fallBackStyle))
                else:
                    self.setStyleSheet(str(self.fallBackStyle))

            if hasattr(self, 'anim'):
                if (self.setIconAnimatedOn == "click" and self.clickPosition == "up") or (self.setIconAnimatedOn == "hover" and self.mousePosition == "out"):
                    try:
                        # print("stopping icon animation")
                        self.anim.stop()
                    except Exception as e:
                        # print(e)
                        pass

    ########################################################################
    ## ANIMATE BUTTON BACKGROUND AND BORDER
    ########################################################################
    def _animate(self, value):
        # print(self, value)
        color_stop = 1
        if self.defaultStyle is not None:
            qss = str(self.defaultStyle)
        else:
            qss = """
            """

        if self.color1 is not None or self.color2 is not None:
            grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1});".format(
                color1=self.color1.name(), color2=self.color2.name(), value=value
            )


            style = """
                border-top-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.466, stop: """+str(value)+"""  """+str(self.color1.name())+""", stop: """+str(color_stop)+"""  """+str(self.color2.name())+""");
                border-bottom-color: qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop: """+str(value)+""" """+str(self.color1.name())+""", stop: """+str(color_stop)+"""  """+str(self.color2.name())+""");
                border-right-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:"""+str(value)+"""  """+str(self.color1.name())+""", stop: """+str(color_stop)+"""  """+str(self.color2.name())+""");
                border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop: """+str(value)+""" """+str(self.color1.name())+""", stop: """+str(color_stop)+"""  """+str(self.color2.name()) +""");
            """

            if self.setObjectAnimate == "border":
                qss += style
            elif self.setObjectAnimate == "background":
                qss += grad
            else:
                qss += grad
                qss += style

            self.setStyleSheet(qss)

            # print(self.color2.name())

    ########################################################################
    ## ANIMATE BUTTON SHADOW
    ########################################################################
    def _animateShadow(self, value):
        # Animate the transition
        self.shadow.setBlurRadius(value)
        #######################################################################
        ## # Appy shadow to button
        ########################################################################
        self.setGraphicsEffect(self.shadow)
########################################################################
##
########################################################################

