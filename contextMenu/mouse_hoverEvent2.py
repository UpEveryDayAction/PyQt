from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class mouseoverEvent(QWidget):
    def __init__(self):
        super().__init__()
        self.stop= False # your 'stop' variable
        self.initUI()

    def initUI(self):
        # self.lbl=QLabel(self)
        # self.lbl.setText("Hover over me to stop the program")
        self.installEventFilter(self)
        self.setGeometry(1000, 30, 300, 100)
        self.setWindowTitle('QLineEdit')
        self.show()

    def eventFilter(self, object, event):
        if event.type()== QEvent.Enter:
            print("Mouse is over the label")
            self.stop= True
            print('program stop is', self.stop)

            self.newWindow()

            return True
        elif event.type()== QEvent.Leave:
            print("Mouse is not over the label")
            self.stop= False
            print('program stop is', self.stop)
        return False

    def newWindow(self):
        self.newWindow = QtWidgets.QMainWindow() 
        """
          File "mouse_hoverEvent2.py", line 25, in eventFilter self.newWindow()
          TypeError: 'QMainWindow' object is not callable
        """
        self.newWindow.setGeometry(100,100,300,300)

if __name__== '__main__':
    app= QApplication(sys.argv)
    ex= mouseoverEvent()
    sys.exit(app.exec_())
# 特定のテキストを含むラベルに対してのみ停止をアクティブにする場合は、eventFilter関数を次のように変更します。



    #サイト:https://www.fixes.pub/program/290226.html