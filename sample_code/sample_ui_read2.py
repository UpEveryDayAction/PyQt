import sys
from PyQt5.QtWidgets import  *
from PyQt5.uic import loadUi
 
class FormTest(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('win.ui',self)
        self.setWindowTitle('MainWin test')
        
 
if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    ft = FormTest()
    ft.show()
    sys.exit(qapp.exec_())
 

