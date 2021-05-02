
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
#from win10toast import ToastNotifier


class AppMainFrame:
    
    def __init__(self):


        self.app = QApplication([])
        
    def push(self):
        self.action2.setChecked(False)


    def MainUI(self):
        self.mainWidget = QWidget()
       

        self.mainWidget.setWindowTitle('My First Application')
        self.mainWidget.move(300, 300)
        self.mainWidget.resize(400, 200)
        #self.mainWidget        

        # 상단 버튼, 레이블 생성, 설정
        onText = 'ON'
        offText = 'OFF'
        labelText = '실시간 검사'
        headText = '문서작업을, 맘편하게'
        projectName = 'DocuFree'

        runButton = QPushButton(onText)
        LabelWidget = QLabel(labelText)
        headlineWidget = QLabel(headText)
        projectWidget = QLabel(projectName)

        #runButton.clicked.connect(self.active)

        # 상단 레이아웃 생성, 설정
        headlineLayout = QVBoxLayout()
        headlineLayout.addWidget(headlineWidget)
        headlineLayout.addWidget(projectWidget)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(runButton)
        buttonLayout.addWidget(LabelWidget)

        highLayout = QHBoxLayout()
        highLayout.addLayout(headlineLayout)
        highLayout.addLayout(buttonLayout)

        # 밑단 버튼, 레이블 생성, 설정
        realOffText = '실시간 검사를 사용 중입니다'
        realOnText = '안전한 문서만 볼 수 있습니다'
        fileDetectText = 'Office 파일 검사'
        #fileDetecBut = QPushButton(fileDetectText)
        

        # 밑단 레이아웃 생성, 설정


        #buttonLayout2 = QVBoxLayout()
        #imageLayout = QVBoxLayout()
        #lowlineLayout = QHBoxLayout()

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(highLayout)
        self.mainWidget.setLayout(mainLayout)


        self.mainWidget.show()




    def run(self):

        self.app.setQuitOnLastWindowClosed(False)


        # Create the icon
        icon = QIcon("image.jpg")


        # Create the tray
        tray = QSystemTrayIcon()
        tray.setIcon(icon)
        tray.setVisible(True)
        

        # Create the Menu
        def FCreate():
            pass
            
            
        def activeFunc():
            toaster = ToastNotifier()
            
            if action2.isChecked():
                toaster.show_toast("DocuFree Notification", "실시간 감지가 실행되고 있습니다." , threaded=True, duration=2)
            else:
                toaster.show_toast("DocuFree Notification", "실시간 감지가 꺼졌습니다." , threaded=True, duration=2)


    
        # System Tray Creat menu 
        menu = QMenu()
        

        # 파일 검사 실행매뉴 생성
        action1 = QAction("파일 검사")
        A = action1.triggered.connect(AppD)
        print(A)

        # 실시간 검사 매뉴 체크 생성
        self.action2 = QAction("실시간 검사", checkable=True)
        self.action2.setChecked(True)
        #action2.triggered.connect(activeFunc)
        

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
