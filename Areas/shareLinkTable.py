#                   Badge Link Creater                  #
#                       myygunduz                       #
#    https://github.com/myygunduz/Badge-Link-Creater    #

from PyQt5.QtWidgets import   QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import   Qt
from Modules.shareLink import  shareLink
from PyQt5.QtWebEngineWidgets import QWebEngineView


class ShareLink(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setAlignment(Qt.AlignCenter)

        self.setLayout(self.mainLayout)

        self.message = QLineEdit()
        self.message.setPlaceholderText('Entry The Share Text')

        self.link = QLineEdit()
        self.link.setPlaceholderText('Entry The Share Link')

        self.button = QPushButton('Create Table')
        self.button.clicked.connect(self.preview)

        self.mainLayout.addWidget(self.message)
        self.mainLayout.addWidget(self.link)
        self.mainLayout.addWidget(self.button)

        self.copyLayout = shareLink()

        self.mainLayout.addLayout(self.copyLayout)
    def preview(self):
        try: self.table.deleteLater()
        except: pass
        self.htmlCode = f"""
<table align='center'>
    <tr>
        <td>
            <a href="https://web.facebook.com/sharer.php?t={self.message.text().replace(" ","%20")}&u={self.link.text()}&_rdc=1&_rdr" onclick="return false;">
                <img src="https://github.com/myygunduz/Badge-Link-Creater/blob/main/Assets/icons/facebook.svg" height="48" width="48" alt="Facebook"/>
            </a>
        </td>
        <td>
            <a href="https://www.facebook.com/dialog/send?link={self.link.text()}&app_id=291494419107518&redirect_uri={self.link.text()}" onclick="return false;">
                <img src="https://github.com/myygunduz/Badge-Link-Creater/blob/main/Assets/icons/messenger.svg" height="48" width="48" alt="Facebook Messenger"/>
            </a>
        </td>
        <td>
            <a href="https://twitter.com/intent/tweet?text={self.message.text().replace(" ","%20")}&url={self.link.text()}" onclick="return false;">
                <img src="https://github.com/myygunduz/Badge-Link-Creater/blob/main/Assets/icons/twitter.svg" height="48" width="48" alt="Twitter"/>
            </a>
        </td>
        <td>
            <a href="https://web.whatsapp.com/send?text={self.message.text().replace(" ","%20")} {self.link.text()}" onclick="return false;">
                <img src="https://github.com/myygunduz/Badge-Link-Creater/blob/main/Assets/icons/whatsapp.svg" height="48" width="48" alt="WhatsApp"/>
            </a>
        </td>
        <td>
            <a href="https://t.me/share/url?url={self.link.text()}&text=G{self.message.text().replace(" ","%20")}" onclick="return false;">
                <img src="https://github.com/myygunduz/Badge-Link-Creater/blob/main/Assets/icons/telegram.svg" height="48" width="48" alt="Telegram"/>
            </a>
        </td>
        <td>
            <a href="https://www.linkedin.com/shareArticle?title={self.message.text().replace(" ","%20")}&url={self.link.text()}" onclick="return false;">
                <img src="https://github.com/myygunduz/Badge-Link-Creater/blob/main/Assets/icons/linkedin.svg" height="48" width="48" alt="LinkedIn"/>
            </a>
        </td>
        <td>
            <a href="https://www.reddit.com/submit?title={self.message.text().replace(" ","%20")}&url={self.link.text()}" onclick="return false;">
                <img src="https://github.com/myygunduz/Badge-Link-Creater/blob/main/Assets/icons/reddit.svg" height="48" width="48" alt="Reddit"/>
            </a>
        </td>
    </tr>
</table>"""
        self.table = QWebEngineView()
        self.table.setHtml(self.htmlCode.strip())
        
        self.mainLayout.addWidget(self.table)
        self.copyLayout.lineEdit.setText(self.htmlCode.replace('onclick="return false;"',""))
        self.copyLayout.lineEdit.setCursorPosition(0)