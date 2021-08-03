import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import time

def clicked():
    print("clicked")

def window():
    app = QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("title")

    label = QtWidgets.QLabel(win)
    label.setText("first label")
    label.move(50,50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("click here")
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())
    s#ys.exit(app.exec_)だと
    # time.sleep(5)
    #ウィンドウがすぐに消えてしまうのでtime

if __name__ == "__main__":
    window()

