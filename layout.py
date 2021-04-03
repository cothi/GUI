"""
작성팀: Server-Agent (한지웅, 박준석)
작성날짜: 2021.04.02
이메일: jiungdev@gmail.com
개발환경: python 3.9.2 64bit
"""

import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog

class DocFree():

    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry("400x450")
        self.NVar = DoubleVar()

    """
    File Create Remove Button Frame 

    파일을 삭제하고 생성하는 버튼을 생성하는 함수입니다.
    """
    def FileCRFrame(self):
        CRFrame = Frame(self.root)
        CRFrame.pack(fill="x")
        CreateButton = Button(CRFrame, text="선택추가")
        RemoveButoon = Button(CRFrame, text="선택삭제")
        CreateButton.pack(side="right")
        RemoveButoon.pack(side="right")

    """
    File List Frame

    작업 목록 파일을 보여주는 기능을 하는 함수입니다.
    """
    def FileListFrame(self):
        ListFrame = Frame(self.root)
        ListFrame.pack(fill="x", padx=7, pady=7)
        scrollbar = Scrollbar(ListFrame)
        scrollbar.pack(side="right", fill="y")
        ListBox = Listbox(ListFrame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
        ListBox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=ListBox.yview)
    
    """
    File Path Set

    파일 경로를 설정해서 해당 파일을 File List에 올려두는 함수입니다.
    """
    def FilePath(self):
        FilePathFrame = LabelFrame(self.root, text="파일저장경로")
        FilePathFrame.pack(fill="x" , padx=7, pady=7)
        FilePathEntry = Entry(FilePathFrame)
        FilePathEntry.pack(side="left", fill="x", expand=True)

    """
    Progress Bar

    파일 악성코드 검사 진행상황을 알려주는 함수입니다.
    """
    def ProgressBar(self):
        ProgressBarFrame = LabelFrame(self.root, text="진행상황")
        ProgressBarFrame.pack(fill="x", padx=7, pady=7 )
            
        self.progress = ttk.Progressbar(ProgressBarFrame, maximum=100, variable=self.NVar)
        self.progress.pack(fill="x", padx=5, pady=5)
    
    """
    Start, Quit Button 
        
    시작, 종료 버튼을 생성하는 함수입니다.
    """
    def StartQuit(self):
        StartQuitFrame = Frame(self.root)
        StartQuitFrame.pack(fill="x")
        
        StartButton = Button(StartQuitFrame, text="시작", command=self.Diagnose)
        QuitButton = Button(StartQuitFrame, text="닫기")

        StartButton.pack(side="left")
        QuitButton.pack(side="right")

    """
    File Diagnose

    파일을 진단하는 함수입니다.
    """
    def Diagnose(self):
        for i in range(0, 100):
            self.NVar.set(i)
            self.progress.update() 
            print(i)

    """
    Run 

    실행을 진행하는 함수입니다.
    """
    def run(self):
        self.root.mainloop()


A = DocFree("DocFree")
A.FileCRFrame()
A.FileListFrame()
A.FilePath()
A.ProgressBar()
A.StartQuit()
A.run()

 
