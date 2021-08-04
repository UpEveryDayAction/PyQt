from test import start_wiget2

if __name__ == '__main__':

    import sys
    app = start_wiget2.QtWidgets.QApplication(sys.argv)
    MainWindow = start_wiget2.QtWidgets.QMainWindow()
    ui = start_wiget2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())