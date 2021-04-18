import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.Qt import *
from PyQt5.QtCore import QBasicTimer
from multiprocessing import Process
from qt_material import apply_stylesheet
from PyQt5.QtGui import *

class AppD(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.listWidget = QListWidget()
        self.phar = QProgressBar()
        self.timer = QBasicTimer()
        self.step = 0
        self.initUI()
        
    
    def initUI(self):
        #
        # QWidgetItem 
        self.setWindowTitle(self.title)
        self.setGeometry(800, 400, 400, 300)
        
     
        """
        self.saveFileDialog()
        """


      
        def AddFunc():
            files = self.openFileNamesDialog()
                    
            if len(files) != 0:
                for i in range(len(files)):
                    print(files[i])
                    item = QListWidgetItem(files[i])
                    item.setCheckState(Qt.Unchecked)
                    self.listWidget.addItem(item)




        def RemoveFunc():
            """
            print(self.listWidget.selectedItems())
              
            for item in self.listWidget.:
                self.listWidget.takeItem(self.listWidget.row(item))
            """
            A = self.listWidget.count()
            count = 0

            for i in range(self.listWidget.count()):
                if self.listWidget.item(i).checkState() == Qt.Checked:
                    count += 1

            while count:
                for i in range(self.listWidget.count()):
                    if self.listWidget.item(i).checkState() == Qt.Checked:
                        self.listWidget.takeItem(i)
                        count -= 1
                        print(count)
                        break

        def RunFunc():
            for i in range(1, 100):
                self.phar.setValue(i)
                time.sleep(0.05)

        font = QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)

        # Create ProgressBar Layout
        self.phar.setGeometry(200, 100, 200, 30)
        ProgressLayout = QHBoxLayout()
        ProgressLayout.addWidget(self.phar)
        

        #Create add Button
        AddButton = QPushButton("파일추가")
        AddButton.setFont(font)
        #AddButton.setGeometry(200, 150, 50, 40)
        AddButton.adjustSize()
        AddButton.clicked.connect(AddFunc)
        
        RemoveButton = QPushButton("선택삭제")
        #RemoveButton.resize(50, 50)
        RemoveButton.setFont(font)
        RemoveButton.clicked.connect(RemoveFunc)

        RunButton = QPushButton()
        RunButton.setText("검사실행")
        RunButton.setFont(font)
        RunButton.clicked.connect(RunFunc)

        CancelButton = QPushButton("닫기")
        CancelButton.setFont(font)
        CancelButton.clicked.connect(self.close)
       
        buttonLayout1 = QVBoxLayout()
        #buttonLayout1.addStretch(2)
        buttonLayout1.addWidget(AddButton)
        buttonLayout1.addWidget(RemoveButton)
        buttonLayout1.addSpacing(400)

        buttonLayout2 = QHBoxLayout()
        buttonLayout2.addStretch(1)
        buttonLayout2.addWidget(RunButton)
        buttonLayout2.addWidget(CancelButton)
            
        # horizontal item, button v stack
        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.listWidget)
        horizontalLayout.addLayout(buttonLayout1)
        
        # Main Box 
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        mainLayout.addLayout(horizontalLayout)
        mainLayout.addLayout(ProgressLayout)
        mainLayout.addSpacing(12)
        mainLayout.addLayout(buttonLayout2)
        self.show()


    def timerEvent(self, event):
        pass

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)

        return files
        

def Create():

    extra = {

    # Button colors
    'danger': '#dc3545',
    'warning': '#ffc107',
    'success': '#17a2b8',
    # Font
    'font-family': 'Roboto',
    'font-size': '5px',
    }   

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_lightgreen.xml", extra=extra)

    ex = AppD()
    #sys.exit(app.exec_())