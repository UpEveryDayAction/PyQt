# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cat_dog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
<<<<<<< Updated upstream
        
=======
>>>>>>> Stashed changes
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(30, 20, 621, 521))
        self.photo.setMaximumSize(QtCore.QSize(761, 521))
        self.photo.setText("")
<<<<<<< Updated upstream
        self.photo.setPixmap(QtGui.QPixmap("image/cat.jpg"))
        self.photo.setObjectName("photo_cat")

  
        self.photo_2 = QtWidgets.QLabel(self.centralwidget)
        self.photo_2.setGeometry(QtCore.QRect(0, 0, 771, 521))
        self.photo_2.setText("")
        self.photo_2.setPixmap(QtGui.QPixmap("image/dog.png"))
        self.photo_2.setObjectName("photo_dog")

        self.photo_3 = QtWidgets.QLabel(self.centralwidget)
        self.photo_3.setGeometry(QtCore.QRect(30, 20, 621, 521))
        self.photo_3.setMaximumSize(QtCore.QSize(761, 521))
        self.photo_3.setText("")
        self.photo_3.setPixmap(QtGui.QPixmap("image/cat.jpg"))
        self.photo_3.setObjectName("photo_cat2")


=======
        self.photo.setPixmap(QtGui.QPixmap("../../../../../Pictures/PhotoScape X/backup-2021-07-28/ドローン0728_ueda_200269_small.jpg"))
        self.photo.setObjectName("photo")
        self.photo_2 = QtWidgets.QLabel(self.centralwidget)
        self.photo_2.setGeometry(QtCore.QRect(0, 0, 771, 521))
        self.photo_2.setText("")
        self.photo_2.setPixmap(QtGui.QPixmap("image/cat.png"))
        self.photo_2.setObjectName("photo_2")
>>>>>>> Stashed changes
        self.cat = QtWidgets.QPushButton(self.centralwidget)
        self.cat.setGeometry(QtCore.QRect(60, 490, 261, 61))
        self.cat.setObjectName("cat")
        self.dog = QtWidgets.QPushButton(self.centralwidget)
        self.dog.setGeometry(QtCore.QRect(420, 500, 261, 61))
        self.dog.setObjectName("dog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cat.setText(_translate("MainWindow", "cat"))
        self.dog.setText(_translate("MainWindow", "dog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
