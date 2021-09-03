from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Manager")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,1350,750)

        self.UI()
        self.show()

    def UI(self):
        pass
    
def main():
    App=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
