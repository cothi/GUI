import rumps
from CheckFilesFrame import DocFree, Create
from multiprocessing import Process
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
from InspectionRealTime import CheckDocument



class AwesomeStatusBarApp(rumps.App):

    def create(self):
        Create()

    @rumps.clicked("설명")
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")

    @rumps.clicked("옵션")
    def onoff(self, sender):
        sender.state = not sender.state
    
    @rumps.clicked("파일 검사")
    def Diagnose(self, _):
        th3 = Process(target=Create)
        th3.start()
        th3.join()

    @rumps.timer(3)
    def NowPrice(self, _):
        A = CheckDocument()
        if A != None:
            print(A)
            rumps.notification("경고", "문서감지", f"{A}, 경로에서 문서가 감지되었습니다")

if __name__ == "__main__":
    AwesomeStatusBarApp("Awesome App").run()
