
"""
작성팀: Server-Agent (한지웅, 박준석)
작성날짜: 2021.04.02
이메일: jiungdev@gmail.com
개발환경: python 3.9.2 64bit
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from CheckFilesFrame import DocFree, Create


class AppMainFrame:
    
    def __init__(self):


        self.app = QApplication([])
        
    

    def run(self):

        self.app.setQuitOnLastWindowClosed(False)



        # Create the icon
        self.icon = QIcon("image.jpg")


        # Create the tray
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)
        


        menu = QMenu()
        action = QAction("A menu item", checkable=True)
  #      action.setChecked(True)
  #      action.triggered.connect(Create)

  #      action2 = QAction("실시간 검사")
#]        action2.triggered.connect(helle)

  #      menu.addAction(action2)
        menu.addAction(action)


        # Add a Quit option to the menu
        quit = QAction("Quit")
        quit.triggered.connect(self.app.quit)
        menu.addAction(quit)


        # Add the menu to the tray
        self.tray.setContextMenu(menu)



        self.app.exec_()


if __name__ == "__main__":

    A = AppMainFrame()
 
    A.AppContent()
    A.TrayContent()
    A.AppContent()
    A.Run()

