from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Manager")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,1350,750)
        self.setFixedSize(self.size())

        self.UI()
        self.show()

    def UI(self):
        self.toolBar()

    def toolBar(self):
        self.tb=self.addToolBar("Tool Bar")
        #############Toolbar Button
        #############Add Product
        self.addProduct=QAction(QIcon('icons/add.png'),"Add Product",self)
        self.tb.addAction(self.addProduct)
        #############Add Member

    
def main():
    App=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
