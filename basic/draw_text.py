import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
# from QtGui import QPainter
from PyQt5.QtCore import Qt
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(600, 300)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        # self.draw_something()
        self.draw_something()


    def draw_something(self):
        from random import randint
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)
        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)
        # painter.drawText(100, 100, 'Hello, world!')
        painter.drawText(100, 100, 100,100,Qt.AlignHCenter,'Hello, world!')
        painter.end()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())