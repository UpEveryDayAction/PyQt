# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow") #外で作ったMainWindowインスタンスにWidgetを貼り付けていっている
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow) #  MainWindow = QtWidgets.QMainWindow()
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget) # centralwidgetにpushButton,checkBoxを貼ってる
        self.pushButton.setGeometry(QtCore.QRect(140, 90, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(130, 220, 93, 19))
        self.checkBox.setObjectName("checkbox1")

        MainWindow.setCentralWidget(self.centralwidget)

        # #####
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)

        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        # ####

        self.retranslateUi(MainWindow)


        # self.pushButton.clicked.connect(self.checkBox.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() #
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

