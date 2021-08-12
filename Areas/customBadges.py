#                   Badge Link Creater                  #
#                       myygunduz                       #
#    https://github.com/myygunduz/Badge-Link-Creater    #

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import  QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import  Qt
from Modules.shareLink import  shareLink
from pyqt5Custom import ImageBox, ToggleSwitch
from PyQt5.QtWebEngineWidgets import QWebEngineView

class CustomBadges(QWidget):
    settings={}
    def __init__(self):
        super().__init__()


        self.mainLayout = QVBoxLayout()
        self.mainLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.mainLayout)

        self.title = QLineEdit()
        self.title.setPlaceholderText('Title')

        self.message = QLineEdit()
        self.message.setPlaceholderText('Message')

        self.moreSettingsButton = ToggleSwitch('Show More Settings')
        self.moreSettingsButton.toggled.connect(self.signalToggleSwitch)


        self.createButton = QPushButton('Create Badge')
        self.createButton.clicked.connect(self.createBadge)

        self.mainLayout.addWidget(self.title)
        self.mainLayout.addWidget(self.message)
        self.mainLayout.addWidget(self.moreSettingsButton)
        self.mainLayout.addWidget(self.createButton)

        self.copyLayout = shareLink()

        self.mainLayout.addLayout(self.copyLayout)

        self.showMoreSettings()
        self.moreSettings.hide()

    

    def createBadge(self):
        self.baseUrl = "https://img.shields.io/static/v1"
        self.baseUrl+= f"?label={self.title.text()}"
        self.baseUrl+= f"&message={self.message.text()}"
        for i in self.settings:
            if len(self.settings[i]) !=0: 
                self.baseUrl +=f"&{self.settings[i][0]}={self.settings[i][-1]}"

        try: self.img.deleteLater()
        except: pass
        try:
            html = f"""
            <html>
            <head></head>
            <body style = "background-color:#f0f0f0;">
                <p align="center">
                    <img src="{self.baseUrl}"/>
                </p>
            </body>
            </html>
            """
            self.img = QWebEngineView()
            self.img.setHtml(html)
            
            self.mainLayout.addWidget(self.img)
            self.copyLayout.lineEdit.setText(f"![{self.title.text().strip()}]({self.baseUrl})")
            self.copyLayout.lineEdit.setCursorPosition(0)
        except KeyError:pass
    def signalToggleSwitch(self):
        
        self.moreSettings.hide()
        if self.moreSettingsButton.isToggled():
            self.moreSettings.show()
    
    def showMoreSettings(self):
        self.moreSettings = QWidget()

        self.moreSettingsLayout = QVBoxLayout()

        self.moreSettings.setLayout(self.moreSettingsLayout)

        self.leftBackgroundColor = QLineEdit()
        self.leftBackgroundColor.setPlaceholderText('Left Background Color')
        self.leftBackgroundColor.textChanged.connect(lambda:self.addSettings(self.leftBackgroundColor,'labelColor',self.leftBackgroundColor.text()))

        self.rightBackgroundColor = QLineEdit()
        self.rightBackgroundColor.setPlaceholderText('Right Background Color')
        self.rightBackgroundColor.textChanged.connect(lambda:self.addSettings(self.rightBackgroundColor,'color',self.rightBackgroundColor.text()))

        self.logo = QLineEdit()
        self.logo.setPlaceholderText('Logo')
        self.logo.textChanged.connect(lambda:self.addSettings(self.logo,'logo',self.logo.text()))

        self.logoColor = QLineEdit()
        self.logoColor.setPlaceholderText('Logo Color')
        self.logoColor.textChanged.connect(lambda:self.addSettings(self.logoColor,'logoColor',self.logoColor.text()))

        self.onlyInt = QIntValidator()
        self.logoWidth = QLineEdit()
        self.logoWidth.setValidator(self.onlyInt)
        self.logoWidth.setPlaceholderText('Logo Width')
        self.logoWidth.textChanged.connect(lambda:self.addSettings(self.logoWidth,'logoWidth',self.logoWidth.text()))

        self.moreSettingsLayout.addWidget(self.leftBackgroundColor)
        self.moreSettingsLayout.addWidget(self.rightBackgroundColor)
        self.moreSettingsLayout.addWidget(self.logo)
        self.moreSettingsLayout.addWidget(self.logoColor)
        self.moreSettingsLayout.addWidget(self.logoWidth)

        self.mainLayout.insertWidget(3,self.moreSettings)

    def addSettings(self, widget, Type, value):
        if len(value.strip()) ==  0:
            try:
                del self.settings[widget]
            except :pass
        else:
            self.settings[widget] = [Type,value]
