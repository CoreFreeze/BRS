from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import Signal
import json

#from main import MainWindow

def loadStyle(self, ui):

    #self.windowAnimationThreadpool = QThreadPool()
    file = open('styleClient.json', )
    data = json.load(file)

    self.ui = ui

    if "MainWindow" in data:
        for mainWindow in data['MainWindow']:
            if "title" in mainWindow and len(str(mainWindow["title"])) > 0:
                self.setWindowTitle(str(mainWindow["title"]))
            if "icon" in mainWindow and len(str(mainWindow["icon"])) > 0:
                self.setWindowIcon(QtGui.QIcon(str(mainWindow["icon"])))
            if "frameless" in mainWindow and mainWindow["frameless"]:
                self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            if "transluscentBg" in mainWindow and mainWindow["transluscentBg"]:
                self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            if "sizeGrip" in mainWindow and len(str(mainWindow["sizeGrip"])) > 0:
                if hasattr(self.ui, str(mainWindow["sizeGrip"])):
                    QSizeGrip(getattr(self.ui, str(mainWindow["sizeGrip"])))
            
            if "navigation" in mainWindow:
                for navigation in mainWindow["navigation"]:
                    if "minimize" in navigation and len(str(navigation["minimize"])) > 0:
                        if hasattr(self.ui, str(navigation["minimize"])):
                            getattr(self.ui, str(navigation["minimize"])).clicked.connect(lambda: self.showMinimized())

                    if "close" in navigation and len(str(navigation["close"])) > 0:
                        if hasattr(self.ui, str(navigation["close"])):
                            getattr(self.ui, str(navigation["close"])).clicked.connect(lambda: self.close())

                    if "restore" in navigation:
                        for restore in navigation["restore"]:
                            if "buttonName" in restore and len(str(restore["buttonName"])) > 0:
                                if hasattr(self.ui, str(restore["buttonName"])):
                                    getattr(self.ui, str(restore["buttonName"])).clicked.connect(lambda: self.restore_or_maximize_window())
                                    self.restoreBtn = getattr(self.ui, str(restore["buttonName"]))
                            if "normalIcon" in restore and len(str(restore["normalIcon"])) > 0:
                                self.normalIcon = str(restore["normalIcon"])
                            else:
                                self.normalIcon = ""

                            if "maximizedIcon" in restore and len(str(restore["maximizedIcon"])) > 0:
                                self.maximizedIcon = str(restore["maximizedIcon"])
                            else:
                                self.maximizedIcon = ""

                    if "moveWindow" in navigation and len(str(navigation["moveWindow"])) > 0:
                        if hasattr(self.ui, str(navigation["moveWindow"])):
                            getattr(self.ui, str(navigation["moveWindow"])).mouseMoveEvent = self.moveWindow

                    if "titleBar" in navigation and len(str(navigation["titleBar"])) > 0:
                        if hasattr(self.ui, str(navigation["titleBar"])):
                            getattr(self.ui, str(navigation["titleBar"])).mouseDoubleClickEvent = self.toggleWindowSize

###############################################################################################################################
#       CustomSlideMenu 
###############################################################################################################################
    if "CustomSlideMenu" in data:
        for customSlide in data['CustomSlideMenu']:
            if "name" in customSlide and len(str(customSlide["name"])) > 0:
                if hasattr(self.ui, str(customSlide["name"])):
                    containerWidget = getattr(self.ui, str(customSlide["name"]))
                    if not containerWidget.metaObject().className() == "CustomSlideMenu":
                        raise Exception("Error: "+str(customSlide["name"])+" is not a CustomSlideMenu object")
                        

                    #
                    defaultWidth = 0
                    defaultHeight = 0
                    collapsedWidth = 0
                    collapsedHeight = 0
                    expandedWidth = 0
                    expandedHeight = 0
                    animationDuration = 0
                    collapsingAnimationDuration = 0
                    expandingAnimationDuration = 0
                    animationEasingCurve = returnAnimationEasingCurve("Linear")
                    collapsingAnimationEasingCurve = returnAnimationEasingCurve("Linear")
                    expandingAnimationEasingCurve = returnAnimationEasingCurve("Linear")
                    buttonObject = ""
                    menuCollapsedIcon = ""
                    menuExpandedIcon = ""
                    relativeTo = ""
                    position = ""
                    shadowColor = ""
                    shadowBlurRadius = ""
                    shadowXOffset = ""
                    shadowYOffset = ""
                    floatMenu = False
                    autoHide = True

                    if "floatPosition" in customSlide:
                        floatMenu = True
                        if hasattr(self, "floatingWidgets"):
                            self.floatingWidgets.append(containerWidget)
                        else:
                            self.floatingWidgets = []
                            self.floatingWidgets.append(containerWidget)

                        for floatPosition in customSlide["floatPosition"]:

                            if "relativeTo" in floatPosition:
                                if hasattr(self.ui, floatPosition["relativeTo"]):
                                    relativeTo = getattr(self.ui, str(floatPosition["relativeTo"]))

                                    relativeTo = containerWidget.setParent(relativeTo)
                                else:
                                    relativeTo = floatPosition["relativeTo"]

                            if "position" in floatPosition:
                                position = floatPosition["position"]

                            if "shadow" in floatPosition:
                                for shadow in floatPosition["shadow"]:
                                    if "color" in shadow:
                                        shadowColor = shadow["color"]
                                    if "blurRadius" in shadow:
                                        shadowBlurRadius = shadow["blurRadius"]
                                    if "xOffset" in shadow:
                                        shadowXOffset = shadow["xOffset"]
                                    if "yOffset" in shadow:
                                        shadowYOffset = shadow["yOffset"]

                            if "autoHide" in floatPosition:
                                if floatPosition["position"] == True:
                                    autoHide = True
                                else:
                                    autoHide = False
                            else:
                                autoHide = False

                    if "defaultSize" in customSlide:
                        for defaultSize in customSlide ["defaultSize"]:

                            if "width" in defaultSize:
                                try:
                                    defaultWidth = int(defaultSize["width"])
                                except:
                                    defaultWidth = defaultSize["width"]
                            if "height" in defaultSize:
                                try:
                                    defaultHeight = int(defaultSize["height"])
                                except:
                                    defaultHeight = defaultSize["height"]


                    if "collapsedSize" in customSlide:
                        for collapsedSize in customSlide["collapsedSize"]:

                            if "width" in collapsedSize:
                                try:
                                    collapsedWidth = int(collapsedSize["width"])
                                except:
                                    collapsedWidth = collapsedSize["width"]

                            if "height" in collapsedSize:
                                try: 
                                    collapsedHeight = int(collapsedSize["height"])
                                except:
                                    collapsedHeight = collapsedSize["height"]

                    if "expandedSize" in customSlide:
                        for expandedSize in customSlide["expandedSize"]:

                            if "width" in expandedSize:
                                try:
                                    expandedWidth = int(expandedSize["width"])
                                except:
                                    expandedWidth = expandedSize["width"]

                            if "height" in expandedSize:
                                try:
                                    expandedHeight = int(expandedSize["height"])
                                except:
                                    expandedHeight = expandedSize["height"]

                    if "menuTransitionAnimation" in customSlide:

                        for menuTransitionAnimation in customSlide["menuTransitionAnimation"]:

                            if "animationDuration" in menuTransitionAnimation:
                                animationDuration = menuTransitionAnimation["animationDuration"]
                                collapsingAnimationDuration = menuTransitionAnimation["animationDuration"]
                                expandingAnimationDuration = menuTransitionAnimation["animationDuration"]

                            if "animationEasingCurve" in menuTransitionAnimation:
                                animationEasingCurve = returnAnimationEasingCurve(menuTransitionAnimation["animationEasingCurve"])
                                collapsingAnimationEasingCurve = returnAnimationEasingCurve(menuTransitionAnimation["animationEasingCurve"])
                                expandingAnimationEasingCurve = returnAnimationEasingCurve(menuTransitionAnimation["animationEasingCurve"])

                            if "whenCollapsing" in menuTransitionAnimation:
                                for whenCollapsing in menuTransitionAnimation["whenCollapsing"]:
                                    if "animationDuration" in whenCollapsing:
                                        collapsingAnimationDuration = whenCollapsing["animationDuration"]

                                    if "animationEasingCurve" in whenCollapsing:
                                        collapsingAnimationEasingCurve = returnAnimationEasingCurve(whenCollapsing["animationEasingCurve"])


                            if "whenExpanding" in menuTransitionAnimation:
                                for whenExpanding in menuTransitionAnimation["whenExpanding"]:
                                    if "animationDuration" in whenExpanding:
                                        expandingAnimationDuration = whenExpanding["animationDuration"]

                                    if "animationEasingCurve" in whenExpanding:
                                        expandingAnimationEasingCurve = returnAnimationEasingCurve(whenExpanding["animationEasingCurve"])

                    containerWidget.customizeCustomSlideMenu(
                        defaultWidth = defaultWidth,
                        defaultHeight = defaultHeight,
                        collapsedWidth = collapsedWidth,
                        collapsedHeight = collapsedHeight,
                        expandedWidth = expandedWidth,
                        expandedHeight = expandedHeight,
                        animationDuration = animationDuration,
                        animationEasingCurve = animationEasingCurve,
                        collapsingAnimationDuration = collapsingAnimationDuration,
                        collapsingAnimationEasingCurve = collapsingAnimationEasingCurve,
                        expandingAnimationDuration = expandingAnimationDuration,
                        expandingAnimationEasingCurve = expandingAnimationEasingCurve,
                        floatMenu = floatMenu,
                        relativeTo = relativeTo,
                        position = position,
                        shadowColor = shadowColor,
                        shadowBlurRadius    = shadowBlurRadius,
                        shadowXOffset   = shadowXOffset,
                        shadowYOffset   = shadowYOffset,
                        autoHide = autoHide
                    )

                    if "toggleButton" in customSlide:
                        for toggleButton in customSlide["toggleButton"]:
                            if "buttonName" in toggleButton and len(str(toggleButton["buttonName"])) > 0:
                                if hasattr(self.ui, str(toggleButton["buttonName"])):

                                    buttonObject = getattr(self.ui, str(toggleButton["buttonName"]))

                                    if "icons" in toggleButton:
                                        for icons in toggleButton["icons"]:
                                            if "whenMenuIsCollapsed" in icons and len(str(icons["whenMenuIsCollapsed"])) > 0:
                                                menuCollapsedIcon = str(icons["whenMenuIsCollapsed"])


                                            if "whenMenuIsExpanded" in icons and len(str(icons["whenMenuIsExpanded"])) > 0:
                                                menuExpandedIcon = str(icons["whenMenuIsExpanded"])

                                    containerWidget.toggleButton(
                                        buttonName = buttonObject,
                                        iconWhenMenuIsCollapsed = menuCollapsedIcon,
                                        iconWhenMenuIsExpanded = menuExpandedIcon,
                                    )

                                else:
                                    raise Exception(str(toggleButton["buttonName"])+" toggle button could not be found")

                    containerWidget.refresh()


                else:
                    raise Exception(str(customSlide["name"])+" is not a QCustomSlideMenu, no widget found")

    if "CustomStackedWidget" in data:
        for customStackedWidget in data['CustomStackedWidget']:
            if "name" in customStackedWidget and len(str(customStackedWidget["name"])) > 0:
                if hasattr(self.ui, str(customStackedWidget["name"])):
                    widget = getattr(self.ui, str(customStackedWidget["name"]))
                    if widget.objectName() == customStackedWidget["name"]:
                        if "transitionAnimation" in customStackedWidget:
                            for transitionAnimation in customStackedWidget["transitionAnimation"]:
                                if "fade" in transitionAnimation:
                                    for fade in transitionAnimation["fade"]:
                                        if "active" in fade and fade["active"]:
                                            widget.fadeTransition = True
                                            if "duration" in fade and fade["duration"] > 0:
                                                widget.fadeTime = fade["duration"]
                                            if "easingCurve" in fade and len(str(fade["easingCurve"])) > 0:
                                                widget.fadeEasingCurve = returnAnimationEasingCurve(fade["easingCurve"])

                        if "navigation" in customStackedWidget:
                            for navigation in customStackedWidget["navigation"]:
                                if "nextPage" in navigation:
                                    if hasattr(self.ui, str(navigation["nextPage"])):
                                        button = getattr(self.ui, str(navigation["nextPage"]))
                                        button.clicked.connect(lambda: widget.slideToNextWidget())
                                    else:
                                        print("No button found")

                                if "previousPage" in navigation:
                                    if hasattr(self.ui, str(navigation["previousPage"])):
                                        button = getattr(self.ui, str(navigation["previousPage"]))
                                        button.clicked.connect(lambda: widget.slideToPreviousWidget())
                                    else:
                                        print("No button found")

                                if "navigationButtons" in navigation:
                                    for navigationButton in navigation["navigationButtons"]:
                                        for button in navigationButton:
                                            widgetPage = navigationButton[button]
                                            if not hasattr(self.ui, str(widgetPage)):
                                                raise Exception("Unknown widget '" +str(widgetPage)+ "'. Please check your JSon file")
                                            if not hasattr(self.ui, str(button)):
                                                raise Exception("Unknown button '" +str(button)+ "'. Please check your JSon file")

                                            pushBtn = getattr(self.ui, str(button))
                                            widgetPg = getattr(self.ui, str(widgetPage))
                                            navigationButtons(widget, pushBtn, widgetPg)

    if "PushButtonGroup" in data:
        grp_count = 0
        for pushButtonGroups in data['PushButtonGroup']:
            if "Buttons" in pushButtonGroups:
                grp_count += 1
                for button in pushButtonGroups["Buttons"]:
                    if hasattr(self.ui, str(button)):
                        btn = getattr(self.ui, str(button))
                        btn.groupParent = self
                        btn.active = False

                        if not btn.metaObject().className() == "QPushButton":
                            raise Exception("Error: "+str(button)+" is not a QPushButton object.")
                            
                        setattr(btn, "group", grp_count)

                        if not hasattr(self, "group_btns_"+str(grp_count)):
                            setattr(self, "group_btns_"+str(grp_count), [])

                        getattr(self, "group_btns_"+str(grp_count)).append(btn)

                        btn.clicked.connect(self.checkButtonGroup)
                    else:
                        raise Exception("Error: Button named"+str(button)+" was not found.")


            activeStyle = ""
            notActiveStyle = ""
            if "Style" in pushButtonGroups:
                for style in pushButtonGroups["Style"]:
                    if "Active" in style:
                        activeStyle = style['Active']
                    if "NotActive" in style:
                        notActiveStyle = style['NotActive']

            getattr(self, "group_btns_"+str(grp_count))[0].active = True
            setattr(self, "group_active_"+str(grp_count), activeStyle)
            setattr(self, "group_not_active_"+str(grp_count), notActiveStyle)
            
def navigationButtons(stackedWidget, pushButton, widgetPage):
    pushButton.clicked.connect(lambda: stackedWidget.setCurrentWidget(widgetPage))

def returnAnimationEasingCurve(easingCurveName):
    if len(easingCurveName) > 0:
        if easingCurveName == "OutQuad":
            return QtCore.QEasingCurve.OutQuad
        elif easingCurveName == "Linear":
            return QtCore.QEasingCurve.Linear
        elif easingCurveName == "InQuad":
            return QtCore.QEasingCurve.InQuad
        elif easingCurveName == "InOutQuad":
            return QtCore.QEasingCurve.InOutQuad
        elif easingCurveName == "OutInQuad":
            return QtCore.QEasingCurve.OutInQuad
        elif easingCurveName == "InCubic":
            return QtCore.QEasingCurve.InCubic
        elif easingCurveName == "OutCubic":
            return QtCore.QEasingCurve.OutCubic
        elif easingCurveName == "InOutCubic":
            return QtCore.QEasingCurve.InOutCubic
        elif easingCurveName == "OutInCubic":
            return QtCore.QEasingCurve.OutInCubic
        elif easingCurveName == "InQuart":
            return QtCore.QEasingCurve.InQuart
        elif easingCurveName == "OutQuart":
            return QtCore.QEasingCurve.OutQuart
        elif easingCurveName == "InOutQuart":
            return QtCore.QEasingCurve.InOutQuart
        elif easingCurveName == "OutInQuart":
            return QtCore.QEasingCurve.OutInQuart
        elif easingCurveName == "InQuint":
            return QtCore.QEasingCurve.InQuint
        elif easingCurveName == "OutQuint":
            return QtCore.QEasingCurve.OutQuint
        elif easingCurveName == "InOutQuint":
            return QtCore.QEasingCurve.InOutQuint
        elif easingCurveName == "InSine":
            return QtCore.QEasingCurve.InSine
        elif easingCurveName == "OutSine":
            return QtCore.QEasingCurve.OutSine
        elif easingCurveName == "InOutSine":
            return QtCore.QEasingCurve.InOutSine
        elif easingCurveName == "OutInSine":
            return QtCore.QEasingCurve.OutInSine
        elif easingCurveName == "InExpo":
            return QtCore.QEasingCurve.InExpo
        elif easingCurveName == "OutExpo":
            return QtCore.QEasingCurve.OutExpo
        elif easingCurveName == "InOutExpo":
            return QtCore.QEasingCurve.InOutExpo
        elif easingCurveName == "OutInExpo":
            return QtCore.QEasingCurve.OutInExpo
        elif easingCurveName == "InCirc":
            return QtCore.QEasingCurve.InCirc
        elif easingCurveName == "OutCirc":
            return QtCore.QEasingCurve.OutCirc
        elif easingCurveName == "InOutCirc":
            return QtCore.QEasingCurve.InOutCirc
        elif easingCurveName == "OutInCirc":
            return QtCore.QEasingCurve.OutInCirc
        elif easingCurveName == "InElastic":
            return QtCore.QEasingCurve.InElastic
        elif easingCurveName == "OutElastic":
            return QtCore.QEasingCurve.OutElastic
        elif easingCurveName == "InOutElastic":
            return QtCore.QEasingCurve.InOutElastic
        elif easingCurveName == "OutInElastic":
            return QtCore.QEasingCurve.OutInElastic
        elif easingCurveName == "InBack":
            return QtCore.QEasingCurve.InBack
        elif easingCurveName == "OutBack":
            return QtCore.QEasingCurve.OutBack
        elif easingCurveName == "InOutBack":
            return QtCore.QEasingCurve.InOutBack
        elif easingCurveName == "OutInBack":
            return QtCore.QEasingCurve.OutInBack
        elif easingCurveName == "InBounce":
            return QtCore.QEasingCurve.InBounce
        elif easingCurveName == "OutBounce":
            return QtCore.QEasingCurve.OutBounce
        elif easingCurveName == "InOutBounce":
            return QtCore.QEasingCurve.InOutBounce
        elif easingCurveName == "OutInBounce":
            return QtCore.QEasingCurve.OutInBounce
        else:
            raise Exception("Unknown value'" +easingCurveName+ "' for setEasingCurve()")
