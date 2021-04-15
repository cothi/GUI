import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
from pystray import MenuItem as item
import pystray
from PIL import Image
import tkinter as tk
from multiprocessing import Process
from CheckFilesFrame import DocFree, Create
class Frame():

    def __init__(self):
        
        self.image = Image.open("image.jpg")
    

    def kkk(self):

        self.menu = pystray.Menu(pystray.MenuItem(("Show"), lambda: self.RunInspection), pystray.MenuItem(("Exit"), lambda: self.exit))
        #menu = (item('upload', action), item('exit', exit))  # 아이콘 클릭시 보여줄 값들 (action,exit는 위쪽 함수의 동작을 가져옴)
        self.icon = pystray.Icon("name", image, "DocuFree", menu)
        
        th2 = Process(target=self.icon.run())
        th2.start()
        th2.join()


    def exit(self):
        self.icon.stop()
    
    
    def RunInspection(self):

        th1 = Process(target = Create)
        th1.start()
        th1.join()


    def action(self):  # 화면 다시 켜짐
        
        self.RunInspection()
        self.icon.stop()
      # 같은 폴터 안에 image.jpg파일이 있어야함




A = Frame()
A.kkk()
