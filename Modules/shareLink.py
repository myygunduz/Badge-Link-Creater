from PyQt5.QtWidgets import  QHBoxLayout, QLineEdit, QPushButton,QApplication
from PyQt5.QtCore import  QTimer
class shareLink(QHBoxLayout):
    def __init__(self):
        super(shareLink,self).__init__()

        self.setSpacing(0)
        self.setContentsMargins(0,0,0,0)

        self.lineEdit = QLineEdit()
        self.lineEdit.setObjectName("shareLink")
        self.lineEdit.setReadOnly(True)

        self.addWidget(self.lineEdit)

        self.copyButton = QPushButton('Copy')
        self.copyButton.setMaximumWidth(50)
        self.copyButton.clicked.connect(self.copyText)

        
        self.addWidget(self.copyButton)

    def copyText(self):
        QApplication.clipboard().setText(self.lineEdit.text())

        self.copyButton.setText('Copied')

        QTimer.singleShot(1000,lambda : self.copyButton.setText('Copy'))
