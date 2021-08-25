#                   Badge Link Creater                  #
#                       myygunduz                       #
#    https://github.com/myygunduz/Badge-Link-Creater    #



from PyQt5.QtWidgets import QScrollArea, QTabWidget, QVBoxLayout, QWidget, QApplication
from Areas import ReadyBadges, CustomBadges, StatsBadges, ShareLink

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600,600)


        self.mainWidget = QTabWidget()

        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0,0,0,0)
        self.setLayout(mainLayout)


        areaOne = ReadyBadges()

        widgetTwo = QScrollArea()
        areaTwo = CustomBadges()
        widgetTwo.setWidget(areaTwo)
        widgetTwo.setContentsMargins(0,0,0,0)
        widgetTwo.setWidgetResizable(True)

        widgetThree = QScrollArea()
        areaThree = StatsBadges()
        widgetThree.setWidget(areaThree)
        widgetThree.setContentsMargins(0,0,0,0)
        widgetThree.setWidgetResizable(True)

        areaFour = ShareLink()

        self.mainWidget.addTab(areaOne,'Ready Badges')
        self.mainWidget.addTab(widgetTwo,'Custom Badges')
        self.mainWidget.addTab(widgetThree,'Github Stats Badges')
        self.mainWidget.addTab(areaFour,'Share Table')
        mainLayout.addWidget(self.mainWidget)

if __name__ == '__main__':
    app = QApplication([])
    window = main()
    window.show()
    app.exec_()