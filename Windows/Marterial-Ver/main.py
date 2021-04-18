
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
from test1 import Create, AppD
from multiprocessing import Process
from PyQt5 import sip
from win10toast import ToastNotifier


class AppMainFrame:
    
    def __init__(self):


        self.app = QApplication([])
        
    

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
        action1.triggered.connect(AppD)

        # 실시간 검사 매뉴 체크 생성
        action2 = QAction("실시간 검사", checkable=True)
        action2.setChecked(True)
        action2.triggered.connect(activeFunc)
        

        # 메인 생성 
        action3 = QAction("DocuFree")
        #action3.triggered.connect(mainC)

        
        # 메뉴 부착
        menu.addAction(action3)
        menu.addAction(action1)
        menu.addAction(action2)

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

