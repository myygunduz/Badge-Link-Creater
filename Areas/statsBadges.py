#                   Badge Link Creater                  #
#                       myygunduz                       #
#    https://github.com/myygunduz/Badge-Link-Creater    #

from PyQt5.QtWidgets import  QComboBox, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtCore import  Qt
from PyQt5.QtGui import QIntValidator
from pyqt5Custom import ToggleSwitch
from Modules.shareLink import  shareLink
from Modules.jsonhelper import readJ
from PyQt5.QtWebEngineWidgets import QWebEngineView


class StatsBadges(QWidget):
    typeDict = {
        'Github Extra Pins':'pin',
        'Top Languages Card':'top-langs',
        'Wakatime Week Stats':'wakatime'
    }
    styleTypeDict =readJ('Database/statsBadgesStyleType.json')
    settings={}
    selectedStyleType = 'default'
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.mainLayout)

        self.username = QLineEdit()
        self.username.setPlaceholderText('Username')

        self.typeBox = QComboBox()
        self.typeBox.addItems(['Select Badge Type','Github Stats','Github Extra Pins','Top Languages Card','Wakatime Week Stats'])

        self.repoName = QLineEdit()
        self.repoName.setPlaceholderText('Perository Name (for Github Extra Pins)')
        self.repoName.textChanged.connect(lambda a:self.addSettings(self.repoName,'repo',self.repoName.text()))
        
        self.moreSettingsButton = ToggleSwitch('Show More Settings')
        self.moreSettingsButton.toggled.connect(self.signalToggleSwitch)

        self.createButton = QPushButton('Create Badge')
        self.createButton.clicked.connect(self.createBadge)


        
        self.mainLayout.addWidget(self.username)
        self.mainLayout.addWidget(self.typeBox)
        self.mainLayout.addWidget(self.repoName)
        self.mainLayout.addWidget(self.moreSettingsButton)
        self.mainLayout.addWidget(self.createButton)

        self.copyLayout = shareLink()

        self.mainLayout.addLayout(self.copyLayout)

    def createBadge(self):
        Type = ""
        if self.typeBox.currentText() in ['Github Extra Pins','Top Languages Card','Wakatime Week Stats']:
            Type = f"/{self.typeDict[self.typeBox.currentText()]}"
            

        self.baseUrl = f"https://github-readme-stats.vercel.app/api{Type}"
        self.baseUrl+= f"?username={self.username.text()}"
        for i in self.settings:
            if len(self.settings[i]) !=0: 
                if i == self.repoName:
                    if self.typeBox.currentText()=='Github Extra Pins':
                        self.baseUrl +=f"&{self.settings[i][0]}={self.settings[i][-1].replace(' ','-')}"
                    
                else:
                    self.baseUrl +=f"&{self.settings[i][0]}={self.settings[i][-1]}"

        try: self.img.deleteLater()
        except: pass
        try:
            html = f"""
            <html>
            <head>
            
            </head>
            <body style = "background-color:#f0f0f0;">
                <p align="center">
                    <img src="{self.baseUrl}"/>
                </p>
            </body>
            </html>
            """
            self.img = QWebEngineView()
            self.img.setHtml(html)
            self.mainLayout.addWidget(self.img,alignment=Qt.AlignVCenter|Qt.AlignHCenter)
            self.copyLayout.lineEdit.setText(f"![{self.username.text().strip()}]({self.baseUrl})")
            self.copyLayout.lineEdit.setCursorPosition(0)
        except KeyError:pass
    def signalToggleSwitch(self):
        try: self.moreSettings.deleteLater()
        except :pass
        if self.moreSettingsButton.isToggled():
            self.showMoreSettings()
    def showMoreSettings(self):
        self.moreSettings = QWidget()

        self.moreSettingsLayout = QVBoxLayout()
        self.moreSettings.setLayout(self.moreSettingsLayout)
        
        
        self.styleTypes = QComboBox()
        self.styleTypes.addItems(self.styleTypeDict.keys())
        self.styleTypes.currentIndexChanged.connect(lambda a:self.signalStyleType(a))

        self.title_color = QLineEdit()
        self.title_color.setPlaceholderText('Title color (Hex Code)')
        self.title_color.textChanged.connect(lambda a: self.addSettings(self.title_color,'title_color',self.title_color.text()))

        self.text_color = QLineEdit()
        self.text_color.setPlaceholderText('Text color (Hex Code)')
        self.text_color.textChanged.connect(lambda a: self.addSettings(self.text_color,'text_color',self.text_color.text()))

        self.icon_color = QLineEdit()
        self.icon_color.setPlaceholderText('Icon color (Hex Code)')
        self.icon_color.textChanged.connect(lambda a: self.addSettings(self.icon_color,'icon_color',self.icon_color.text()))

        self.border_color = QLineEdit()
        self.border_color.setPlaceholderText('Bitle color (Hex Code)')
        self.border_color.textChanged.connect(lambda a: self.addSettings(self.border_color,'border_color',self.border_color.text()))

        self.bg_color = QLineEdit()
        self.bg_color.setPlaceholderText('Background Color (Hex Code)')
        self.bg_color.textChanged.connect(lambda a: self.addSettings(self.bg_color,'bg_color',self.bg_color.text()))

        self.hide_color = QLineEdit()
        self.hide_color.setPlaceholderText('Hide Color (Hex Code)')
        self.hide_color.textChanged.connect(lambda a: self.addSettings(self.hide_color,'hide_color',self.hide_color.text()))

        self.onlyInt = QIntValidator()
        self.border_radius  = QLineEdit()
        self.border_radius.setValidator(self.onlyInt)
        self.border_radius.setPlaceholderText('Border Radius')
        self.border_radius.textChanged.connect(lambda a: self.addSettings(self.border_radius,'border_radius',self.border_radius.text()))

        self.moreSettingsLayout.addWidget(self.styleTypes)
        self.moreSettingsLayout.addWidget(self.title_color)
        self.moreSettingsLayout.addWidget(self.text_color)
        self.moreSettingsLayout.addWidget(self.icon_color)
        self.moreSettingsLayout.addWidget(self.border_color)
        self.moreSettingsLayout.addWidget(self.bg_color)
        self.moreSettingsLayout.addWidget(self.hide_color)
        self.moreSettingsLayout.addWidget(self.border_radius)

        self.mainLayout.insertWidget(3,self.moreSettings)

    def signalStyleType(self,index):
        self.selectedStyleType = self.styleTypeDict[list(self.styleTypeDict.keys())[index]]
        self.addSettings(self.styleTypes, 'theme', self.selectedStyleType)

    def addSettings(self, widget, Type, value):
        if len(value.strip()) ==  0:
            try:
                del self.settings[widget]
            except :pass
        else:
            self.settings[widget] = [Type,value]