import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import time

app = QApplication(sys.argv)
win=QMainWindow()
win.setGeometry(200,200,300,300)
win.setWindowTitle("title")
win.show()
#time.sleep(5)
#ウィンドウがすぐに消えてしまうのでtime
sys.exit(app.exec_())

