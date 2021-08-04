#import start_wiget2
#import test.start_wiget2
from test import test1

if __name__ == '__main__':

    import sys
    app = test1.QtWidgets.QApplication(sys.argv)
    MainWindow = test1.QtWidgets.QMainWindow()
    ui = test1.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())