
"""
작성팀: Server-Agent (한지웅, 박준석)
작성날짜: 2021.04.02
이메일: jiungdev@gmail.com
개발환경: python 3.9.2 64bit
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from CheckFilesFrame import DocFree, Create
from qt_material import apply_stylesheet
from CheckFileFrame import Create, AppD
from multiprocessing import Process
from PyQt5 import sip
from win10toast import ToastNotifier
import time

class AppMainFrame:
    
    def __init__(self):


        self.app = QApplication([])
        self.toaster = ToastNotifier()

    def push(self):
        self.action2.setChecked(False)


    def MainUI(self):
        self.mainWidget = QWidget()
        self.mainWidget.setWindowTitle('DocuFree Application')
        self.mainWidget.move(300, 300)
        self.mainWidget.resize(700, 300)
        #self.mainWidget        

        # 좌측: 버튼, 레이블 생성,Css 설정
        
        headText = '문서작업을, 맘편하게'
        projectName = 'DocuFree'
        fileDetectText = 'Office 파일 검사'
        self.onStyleSheet = 'QPushButton{background-color: #a5d068; color: white; border: 0px solid;}'
        self.offStyleSheet = 'QPushButton{background-color: #ea5b60; color: white; border: 0px solid;}'
       
        
        headlineWidget = QLabel(headText)
        headlineWidget.setStyleSheet('font-weight: 500; font-size: 11px;')
        projectWidget = QLabel(projectName)
        projectWidget.setStyleSheet('font-weight: 900; font-size: 30px;')
        
        fileDetecButt = QPushButton(fileDetectText)
        fileDetecButt.setStyleSheet('''
        QPushButton{height: 170px; width:200px; background-color:#bef67a; color:#232629; padding-bottom: 0px; margin-bottom:100px; border: 0px solid;}
        QPushButton:hover { background-color: #d9f0be;}
        ''')
        fileDetecButt.clicked.connect(AppD)

        # 좌측: 레이아웃 생성, 설정
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(headlineWidget)
        leftLayout.addWidget(projectWidget)
        leftLayout.addWidget(fileDetecButt)
        leftLayout.setContentsMargins(10,10,0,50)
        leftLayout.setSpacing(0)




        

        # 우측 버튼, 레이블 생성, 이미지 경로 설정
        realOffText = '실시간 검사를 사용 중입니다'
        realOnText = '안전한 문서만 볼 수 있습니다'
        self.realOnNofiText = '실시간 검사를 사용 중입니다'
        self.realOnNofiSupoText ='안전한 문서만 볼 수 있습니다'
        self.realOffNofiText = '실시간 검사가 동작하지 않습니다'
        self.realOffNofiSupoText = '안적하지 않은 문서를 확인 할 수도 있습니다'
        self.onText = 'ON'
        self.offText = 'OFF'
        labelText = '          실시간 검사'

        imageOffUrl = 'C:\\Users\\hanjiung\\project\\test\\image\\shield_warning.png'
        imageOnUrl= 'C:\\Users\\hanjiung\\project\\test\\image\\shield.png'
        
        LabelWidget = QLabel(labelText)
        LabelWidget.setStyleSheet('font-weight:bold; background-color: #414344')

        self.onStyleSheet = 'QPushButton{background-color: #a5d068; color: white; border: 0px solid;}'
        self.offStyleSheet = 'QPushButton{background-color: #ea5b60; color: white; border: 0px solid;}'
    
        self.runButton = QPushButton(self.onText)
        self.runButton.setStyleSheet(self.onStyleSheet)
        self.runButton.clicked.connect(self.activeRun)

        self.realOnImage = QPixmap(imageOnUrl).scaledToWidth(100)
        self.realOffImage = QPixmap(imageOffUrl).scaledToWidth(100)
        self.label = QLabel()
        self.label.setPixmap(self.realOnImage)
        self.label.setContentsMargins(130,80,0,0)

        self.OnOffTextLabel = QLabel(self.realOnNofiText)
        self.OnOffTextLabel.setStyleSheet('margin-bottom: 20px; margin-left: 68px; padding-bottom:-40px; font-size: 17px; font-weight:1000')
        self.OnOffSupoTextLabel = QLabel(self.realOnNofiSupoText)
        self.OnOffSupoTextLabel.setStyleSheet('margin-bottom: 100px; margin-left: 110px;')
        
        #self.label.resize(50, 50)
        

        # 우측 레이아웃 생성, 설정
        rightLayout = QVBoxLayout()

        onOffLayout = QHBoxLayout()
        onOffLayout.addWidget(LabelWidget)
        onOffLayout.addWidget(self.runButton)
        onOffLayout.setSpacing(0)
        onOffLayout.setContentsMargins(0,7,0,0)

        rightLayout.addLayout(onOffLayout)
        rightLayout.addWidget(self.label)
        rightLayout.addWidget(self.OnOffTextLabel)
        rightLayout.addWidget(self.OnOffSupoTextLabel)
        rightLayout.setSpacing(0)
        
        
        
        mainLayout = QHBoxLayout()
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)

        self.mainWidget.setLayout(mainLayout)
        self.mainWidget.show()


    def activeRun(self):
        if self.action2.isChecked():
            self.action2.setChecked(False)
            self.runButton.setText(self.offText)
            self.runButton.setStyleSheet(self.offStyleSheet)
            self.label.setPixmap(self.realOffImage)
            self.OnOffTextLabel.setText(self.realOffNofiText)
            self.OnOffSupoTextLabel.setText(self.realOffNofiSupoText)
            time.sleep(0.4)
            self.activeFunc()
            
        else:
            self.action2.setChecked(True)
            self.runButton.setText(self.onText)
            self.runButton.setStyleSheet(self.onStyleSheet)
            self.label.setPixmap(self.realOnImage)
            self.OnOffTextLabel.setText(self.realOnNofiText)
            self.OnOffSupoTextLabel.setText(self.realOnNofiSupoText)
            time.sleep(0.4)
            self.activeFunc()
            #self.runButton.clicked.connect(self.activeRun)

    """
    # active2 체크버튼 동기화
    def checkSyc(self):
        if self.action2.isChecked():
            self.action2.setChecked(False)
        else:
            self.action2.setChecked(True)
    """

    def activeFunc(self):
            if self.action2.isChecked():
                self.toaster.show_toast("DocuFree Notification", "실시간 감지가 실행되고 있습니다." , threaded=True, duration=1.5)
            else:
                self.toaster.show_toast("DocuFree Notification", "실시간 감지가 꺼졌습니다." , threaded=True, duration=1.5)


    def run(self):

        self.app.setQuitOnLastWindowClosed(False)


        # Create the icon
        icon = QIcon("icon.png")


        # Create the tray
        tray = QSystemTrayIcon()
        tray.setIcon(icon)
        tray.setVisible(True)
        

        # Create the Menu
        def FCreate():
            pass
            
            

    
        # System Tray Creat menu 
        menu = QMenu()
        

        # 파일 검사 실행매뉴 생성
        action1 = QAction("파일 검사")
        A = action1.triggered.connect(AppD)
        print(A)

        # 실시간 검사 매뉴 체크 생성
        self.action2 = QAction("실시간 검사", checkable=True)
        self.action2.setChecked(True)
        self.action2.triggered.connect(self.activeFunc)
        

        # 메인 생성 
        action3 = QAction("DocuFree")
        action3.triggered.connect(self.MainUI)

        
        # 메뉴 부착
        menu.addAction(action3)
        menu.addAction(action1)
        menu.addAction(self.action2)

        # Add a Quit option to the menu
        quit = QAction("종료")
        quit.triggered.connect(self.app.quit)
        menu.addAction(quit)


        # Add the menu to the tray
        tray.setContextMenu(menu)

        apply_stylesheet(self.app, theme="dark_lightgreen.xml")
        self.app.exec_()


A = AppMainFrame()
A.run()

