import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import *
from PyQt5.Qt import *
#from main import *


class DocuFreeWidget:

    def __init__(self):
        self.mainWidget = QWidget()
        self.initUI()
        self.check = True     
    
    def initUI(self):

        self.mainWidget.setWindowTitle('My First Application')
        self.mainWidget.move(300, 300)
        self.mainWidget.resize(400, 200)
        #self.mainWidget        

        # 상단 버튼, 레이블 생성, 설정
        self.onText = 'ON'
        self.offText = 'OFF'
        labelText = '실시간 검사'
        headText = '문서작업을, 맘편하게'
        projectName = 'DocuFree'

       
        self.runButton = QPushButton(self.onText)
        LabelWidget = QLabel(labelText)
        headlineWidget = QLabel(headText)
        projectWidget = QLabel(projectName)

        self.runButton.clicked.connect(self.activeRun)

        # 상단 레이아웃 생성, 설정
        headlineLayout = QVBoxLayout()
        headlineLayout.addWidget(headlineWidget)
        headlineLayout.addWidget(projectWidget)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(LabelWidget)
        buttonLayout.addWidget(self.runButton)

        highLayout = QHBoxLayout()
        highLayout.addLayout(headlineLayout)
        highLayout.addLayout(buttonLayout)

        # 밑단 버튼, 레이블 생성, 설정
        realOffText = '실시간 검사를 사용 중입니다'
        realOnText = '안전한 문서만 볼 수 있습니다'
        fileDetectText = 'Office 파일 검사'
        imageOffUrl = 'image/trayOn.png'
        imageOnUrl = 'image/trayOff.png'
        self.realOnImage = QPixmap(imageOnUrl).scaledToWidth(200)
        self.realOffImage = QPixmap(imageOffUrl).scaledToWidth(200)
        self.label = QLabel()
        self.label.setPixmap(self.realOnImage)
        self.label.resize(50, 50)
        fileDetecButt = QPushButton(fileDetectText)
         

        # 밑단 레이아웃 생성, 설정
        buttonLayout2 = QVBoxLayout()
        imageLayout = QVBoxLayout()
        lowlineLayout = QHBoxLayout()

        buttonLayout2.addWidget(fileDetecButt)
        imageLayout.addWidget(self.label) 
        
        lowlineLayout.addLayout(buttonLayout2)
        lowlineLayout.addLayout(imageLayout)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(highLayout)
        mainLayout.addLayout(lowlineLayout)

        self.mainWidget.setLayout(mainLayout)
        self.mainWidget.show()


    def activeRun(self):
        if self.check:
            self.check = False
            self.runButton.setText(self.offText)
            self.label.setPixmap(self.realOffImage)
        else:
            self.check = True
            self.runButton.setText(self.onText)
            self.label.setPixmap(self.realOnImage)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DocuFreeWidget()
    sys.exit(app.exec_())
