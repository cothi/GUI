import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.Qt import *
from PyQt5.QtCore import QBasicTimer
from multiprocessing import Process

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 700
        self.height = 640
        self.listWidget = QListWidget()
        self.phar = QProgressBar()
        self.phar.setGeometry(30, 40, 300, 25)
        self.timer = QBasicTimer()
        self.step = 0
        self.initUI()
        
    
    def initUI(self):
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        """
     
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
                time.sleep(0.5)

        # Create ProgressBar
        ProgressLayout = QHBoxLayout()
        ProgressLayout.addWidget(self.phar)
        

        #Create add Button
        AddButton = QPushButton("Add")
        AddButton.clicked.connect(AddFunc)
        
        RemoveButton = QPushButton("Remove")
        RemoveButton.clicked.connect(RemoveFunc)

        RunButton = QPushButton("Run")
        RunButton.clicked.connect(RunFunc)
        CancelButton = QPushButton("Cancel")
        CancelButton.clicked.connect(self.close)
       
        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addStretch(2)
        buttonLayout1.addWidget(AddButton)
        buttonLayout1.addWidget(RemoveButton)
        buttonLayout1.addSpacing(300)

        buttonLayout2 = QHBoxLayout()
        buttonLayout2.addStretch(1)
        buttonLayout2.addWidget(RunButton)
        buttonLayout2.addWidget(CancelButton)
            
        # horizontal item, button v stack
        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.listWidget, 1)
        horizontalLayout.addLayout(buttonLayout1)
        
        # Main Box 
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
        self.setLayout(mainLayout)
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
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
