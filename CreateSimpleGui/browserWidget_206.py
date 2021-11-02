from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys,os

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)

        navtb = QToolBar("Navigation")
        navtb.setIconSize( QSize(16,16) )
        self.addToolBar(navtb)      
        back_btn = QAction( QIcon(os.path.join('icons','arrow.jpg')), "Back\
        ", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect( self.browser.back )
        navtb.addAction(back_btn)
        self.show()
app = QApplication(sys.argv)
window = MainWindow()
app.exec_()