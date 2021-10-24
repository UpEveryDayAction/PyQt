from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        layout = QVBoxLayout()

        for n in range(10):
            btn = QPushButton(str(n))
            btn.pressed.connect( lambda n=n: self.my_custom_fn(n) )
            # ex) n=4としたself.mycustom_fn(self,4)にコネクトするようになる
            # btn.pressed.connect( lambda: self.my_custom_fn(n) )

            layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def my_custom_fn(self, n):
        print("Button %d was clicked" % n)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())