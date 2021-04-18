import os      
import pathlib

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.textEditTotalPDFnumber = QtWidgets.QTextEdit('QTextEdit')
        self.textEditTotalPDFnumber.setReadOnly(True)

        self.listWidgetPDFlist = QtWidgets.QListWidget()

        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.addWidget(self.listWidgetPDFlist)
        self.vlayout.addWidget(self.textEditTotalPDFnumber)

        self.btnAddItems = QtWidgets.QPushButton()
        self.btnAddItems.setText('add items')
        self.vlayout.addWidget(self.btnAddItems)
        self.btnAddItems.clicked.connect(self.addItems)

        self.btnPrintItems = QtWidgets.QPushButton()
        self.btnPrintItems.setText('print the total number of checked items')
        self.vlayout.addWidget(self.btnPrintItems)
        self.btnPrintItems.clicked.connect(self.printItems)

        ### +++++++++++++++++++++++++++++++++++++++++++++++
        self.btnShowSelectedFile = QtWidgets.QPushButton()
        self.btnShowSelectedFile.setText('Show selected file')
        self.vlayout.addWidget(self.btnShowSelectedFile)
        self.btnShowSelectedFile.clicked.connect(self.fileListSelected)        

        self.setLayout(self.vlayout)

    def addItems(self):
        Files = ["file1.txt", "file2.py", "file3.txt",]
        self.textEditTotalPDFnumber.append("\naddItems --> Files {}".format(Files))

        self.ListFilesInViewer(Files)

    def ListFilesInViewer(self, Files):              
        for itemFile in Files:
            item = QtWidgets.QListWidgetItem(itemFile)
            item.setCheckState(QtCore.Qt.Unchecked)  #Unchecked
            item.setText('{}'.format(str(itemFile), str(self.listWidgetPDFlist.count())))
            self.listWidgetPDFlist.addItem(item)  # listWidgetPDFlist

    ### ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
    def fileListSelected(self):             # Function to select the desired file from the list in the left pane
        """
        ListIterator=range(self.listWidgetPDFlist.count() -1)
        for index in ListIterator:
            p = pathlib.Path(self.fullPath)
            print(" FILE SELECTED this is P==>{}".format(p))
            oneDir = os.path.join(*p.parts[:-2])
            print("FILE SELECTED this is oneDir==>{}".format(oneDir))            
            Item= oneDir + "\\" + self.listWidgetPDFlist.selectedItems()[index].text()
            print("FILE SELECTED this is the cuurent Item =={}".format(Item))            
            print("current row = {}".format(self.listWidgetPDFlist.currentRow()))
            self.mouseHover()
            return Item            
        """
        #p = pathlib.Path(self.fullPath) 
        p = pathlib.Path(os.getcwd())  
        self.textEditTotalPDFnumber.append("\n FILE SELECTED this is   P              =>`{}`".format(p))
        oneDir = os.path.join(*p.parts[:-2])
        self.textEditTotalPDFnumber.append(" FILE SELECTED this is   oneDir      =>`{}`".format(oneDir))   
        self.textEditTotalPDFnumber.append("listWidgetPDFlist.selectedItems     =>`{}`".format(self.listWidgetPDFlist.selectedItems()))
        #Item = oneDir + "\\" + self.listWidgetPDFlist.selectedItems()[index].text()
        if self.listWidgetPDFlist.selectedItems():
            Item = oneDir + "\\" + self.listWidgetPDFlist.selectedItems()[0].text()
            self.textEditTotalPDFnumber.append(" FILE SELECTED this is the cuurent Item =>`<b>{}</b>`\n".format(Item))
            #self.mouseHover()
            #return Item
        else:
            self.textEditTotalPDFnumber.append("<b>!!! NO SELECTED FILE !!!</b>\n")

    def printItems(self):
        checkedItem = 0

        for index in range(self.listWidgetPDFlist.count()):
            if self.listWidgetPDFlist.item(index).checkState() == QtCore.Qt.Checked:
                 checkedItem += 1        

        self.textEditTotalPDFnumber.append("\nchecked items --> {}".format(str(checkedItem)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec_())
