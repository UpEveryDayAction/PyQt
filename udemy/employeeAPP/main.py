from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QFont
import sys
import sqlite3

con=sqlite3.connect('employees.db')
cur = con.cursor()


class Main(QWidget): # tip self=Mainインスタンス
    def __init__(self):
        super().__init__()
        self.setWindowTitle("kkk")
        self.setGeometry(450,150,750,600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesighn()
        self.layouts()
        
    def mainDesighn(self):
        self.employeeList=QListWidget()
        self.btnNew=QPushButton("New")
        self.btnNew.clicked.connect(self.addEmployee)
        self.btnUpdate=QPushButton("Update")
        self.btnDelete=QPushButton("Delete")

    def layouts(self):
        ###################Layouts
        self.mainLayout=QHBoxLayout()
        self.leftLayout=QFormLayout()
        self.rightMainLayout=QVBoxLayout()
        self.rightTopLayout=QHBoxLayout()
        self.rightBottomLayout=QHBoxLayout()
        ###################Child Layouts to main Layout
        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        self.mainLayout.addLayout(self.leftLayout,40) ##tip 割合を入れることができる
        self.mainLayout.addLayout(self.rightMainLayout,60)

        ##########################adding wigdets to Layout
        self.rightTopLayout.addWidget(self.employeeList)
        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnUpdate)
        self.rightBottomLayout.addWidget(self.btnDelete)
        ####################setting main window Layout
        self.setLayout(self.mainLayout)
    
    def addEmployee(self):
        self.newEmployee=AddEmployee()
        self.close()

class AddEmployee(QWidget):
    def __init__(self): #tip self=AddEmployeeインスタンス
        super().__init__()
        self.setWindowTitle("Add Employees")
        self.setGeometry(450,150,350,600)
        self.UI()
        self.show()   

    def UI(self):
        self.mainDesign()
        self.layouts()

    def mainDesign(self):
        pass
    
    def layouts(self):
        ###################################creating main Layout
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout=QFormLayout()
        ######################################adding child layouts to main layout
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        ###################################setting main layout for widow
        self.setLayout(self.mainLayout)

def main():
    APP=QApplication(sys.argv)
    window=Main()
    sys.exit(APP.exec_())

if __name__ == '__main__':
    main()