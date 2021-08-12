#                   Badge Link Creater                  #
#                       myygunduz                       #
#    https://github.com/myygunduz/Badge-Link-Creater    #

from PyQt5.QtWidgets import   QLineEdit, QVBoxLayout, QWidget, QCompleter
from PyQt5.QtCore import   Qt
from Modules.jsonhelper import  readJ
from Modules.shareLink import  shareLink
from PyQt5.QtWebEngineWidgets import QWebEngineView
class ReadyBadges(QWidget):
    def __init__(self):
        super().__init__()
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(self.mainLayout)

        self.readyBadgesDictionary = readJ('Database/readyBadges.json')

        self.lineEdit = QLineEdit()
        self.lineEdit.returnPressed.connect(self.previewBadge)
        self.lineEdit.setPlaceholderText('Type The Platform Name')

        self.completer = QCompleter([i for i in self.readyBadgesDictionary])

        self.lineEdit.setCompleter(self.completer)

        self.mainLayout.addWidget(self.lineEdit)

        self.copyLayout = shareLink()
        self.mainLayout.addLayout(self.copyLayout)

    def previewBadge(self):
        try: self.img.deleteLater()
        except: pass
        try:
            html = f"""
            <html>
            <head></head>
            <body style = "background-color:#ffffff;">
                <p align="center">
                    <img src="{self.readyBadgesDictionary[self.lineEdit.text()][-1]}"/>
                </p>
            </body>
            </html>
            """
            self.img = QWebEngineView()
            self.img.setHtml(html)
            self.mainLayout.addWidget(self.img)
            self.copyLayout.lineEdit.setText(self.readyBadgesDictionary[self.lineEdit.text()][0])
            self.copyLayout.lineEdit.setCursorPosition(0)
        except KeyError:pass








