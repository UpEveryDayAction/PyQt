import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
# from QtGui import QPainter
from PyQt5.QtCore import Qt
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        # self.draw_something()
        self.draw_something()

    # def draw_something(self):
    #     painter = QtGui.QPainter(self.label.pixmap())
    #     pen = QtGui.QPen()
    #     pen.setWidth(40)
    #     pen.setColor(QtGui.QColor('red'))
    #     painter.setPen(pen)
    #     painter.drawPoint(200, 150)
    #     painter.end()

    # def draw_something2(self):
    #     from random import randint
    #     painter = QtGui.QPainter(self.label.pixmap())
    #     pen = QtGui.QPen()
    #     pen.setWidth(3)
    #     painter.setPen(pen)
    #     for n in range(10000):
    #         painter.drawPoint(
    #         200+randint(-100, 100), # x
    #         150+randint(-100, 100) # y
    #         )
    #     painter.end()

    def draw_something(self):
        from random import randint
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(15)
        pen.setColor(QtGui.QColor('blue'))
        painter.setPen(pen)
        painter.drawLine(
        QtCore.QPoint(100, 100),
         QtCore.QPoint(300, 200)
         )
        painter.end()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())