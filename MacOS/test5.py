import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic


class WindowClass() :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #ProgressBar? ???
        self.progressBar_Test.valueChanged.connect(self.printValue)

        #QTimer? ???? ???? ProgressBar? ?? 1? ???? ?????.
        #QTimer?Interval? 1000?? ??? ?, ProgrssBar? ?? ???? ?? ??? ???? QTimer? ?????.
        #QTimer? ?? ??? 02.17.01 QTimer?? ?? ? ????.
        self.timerVar = QTimer()
        self.timerVar.setInterval(1000)
        self.timerVar.timeout.connect(self.progressBarTimer)
        self.timerVar.start()

    def progressBarTimer(self) :
        self.time = self.progressBar_Test.value()
        self.time += 1
        self.progressBar_Test.setValue(self.time)

        #ProgressBar? ?? ??? ??? ?? Timer? ???? ProgressBar? ?? ??? ???? ?? ???.
        if self.time >= self.progressBar_Test.maximum() :
            self.timerVar.stop()

    def printValue(self) :
        print(self.progressBar_Test.value())

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
