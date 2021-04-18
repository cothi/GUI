import sys
from PyQt5.QtCore import QDate, QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class VerifyDialog(QDialog):
    def __init__(self, parent=None):
        super(VerifyDialog, self).__init__(parent)

        self.listWidget = QListWidget()

       y self.listWidget.itemEntered.connect(lambda item: item.setCheckState(Qt.Checked if item.checkState()==Qt.Unchecked else Qt.Unchecked))


        for i in range(100):
            item = QListWidgetItem("Item %i" % i)
            # could be Qt.Unchecked; setting it makes the check appear
            item.setCheckState(Qt.Checked)
            self.listWidget.addItem(item)
        
        def Run():
            print("123")
        
        runButton = QPushButton("Run")
        runButton.clicked.connect(Run)

        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.close)

        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.listWidget, 1)

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(runButton)
        buttonsLayout.addWidget(cancelButton)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
        mainLayout.addSpacing(12)
        mainLayout.addLayout(buttonsLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle("Config Dialog")
        self.show()


if __name__=="__main__":
    app = QApplication(sys.argv)
    dialog = VerifyDialog()
    sys.exit(app.exec_())
