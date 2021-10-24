import sys
from PyQt5 import QtGui,QtWidgets
from PyQt5 import QtCore

class Window (QtWidgets.QWidget):
    def __init__(self, parent=None):        

        super(Window, self).__init__(parent)

        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setObjectName('listWidget')

        self.lbl = QtWidgets.QLabel(self)
        self.lbl.installEventFilter

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 220, 101, 23))
        self.pushButton.setObjectName('pushButton')
        self.pushButton.setText('Add')

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName ('verticalLayout')        

        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout.addWidget(self.pushButton)


        #Right click menu
        self.listWidget.setContextMenuPolicy (QtCore.Qt.CustomContextMenu)        
        self.listWidget.customContextMenuRequested.connect (self.rightClickFunction)                     

        self.action = QtWidgets.QAction (self)
        self.action.setObjectName('action')        
        self.action.setText ('Open')

        self.action1 = QtWidgets.QAction (self)
        self.action1.setObjectName('action1')        
        self.action1.setText ('Test')  

        self.customMenu = QtWidgets.QMenu('Menu', self.listWidget)       
        self.customMenu.addAction (self.action)
        self.customMenu.addAction (self.action1)

        #self.customMenu.addAction (QtGui.QIcon(''), 'Open', (self.oepnFunction))          
        #self.customMenu.addAction (QtGui.QIcon(''), 'Test', (self.testFunction))      

        self.pushButton.clicked.connect (self.addItem)
        self.action.triggered.connect (self.oepnFunction)
        self.action1.triggered.connect (self.testFunction)

        #void changed ()
        #void hovered ()
        #void toggled (bool)
        #void triggered (bool = 0)


    def addItem (self) :
        count   = int (self.listWidget.count ())         
        self.listWidget.addItem (str(count+1) + '_')


    def rightClickFunction (self, event) :
        index = self.listWidget.indexAt (event)
        if not index.isValid():
            return
        item = self.listWidget.indexAt(event)
        self.customMenu.popup (QtGui.QCursor.pos())       


    def oepnFunction (self) :
        print("hai............open")

    def testFunction (self) :
        print("hai............test")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())

# PyQt4から書き換えました
#https://stackoverflow.com/questions/38640903/pyqt-how-do-i-change-the-customcontextmenu-trigger