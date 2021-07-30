import sys
from PyQt5.QtWidgets import  *
 
 
def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.setWindowTitle('Window01')
 
    WiNum = QLCDNumber()
    BoxLay = QVBoxLayout()
    BoxLay.addWidget(WiNum)
    w.setLayout(BoxLay)
 
    WiNum.display(3.14)
 
    w.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
 

