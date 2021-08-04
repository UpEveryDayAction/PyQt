# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_wige2t.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/cat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("MainWindow\n"
"{\n"
"color: rgb(254, 254, 254);\n"
"    background-color: rgb(53, 53, 53);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 255, 127);\n"
"color: rgb(61, 61, 61);")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, -10, 321, 151))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.functionGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.functionGroupBox.setGeometry(QtCore.QRect(70, 160, 271, 271))
        self.functionGroupBox.setAutoFillBackground(False)
        self.functionGroupBox.setStyleSheet("QGroupBox\n"
"{\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(166, 166, 166);\n"
"    border-style: none;\n"
"    padding-top: 10px;\n"
"}")
        self.functionGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.functionGroupBox.setObjectName("functionGroupBox")
        self.radioButton = QtWidgets.QRadioButton(self.functionGroupBox)
        self.radioButton.setGeometry(QtCore.QRect(22, 65, 180, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("    background-color: rgb(166, 166, 166); \n"
"")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.functionGroupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(22, 115, 180, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("    background-color: rgb(166, 166, 166); \n"
"")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.functionGroupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(22, 165, 180, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("    background-color: rgb(166, 166, 166); \n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.settingGroupBpx = QtWidgets.QGroupBox(self.centralwidget)
        self.settingGroupBpx.setGeometry(QtCore.QRect(410, 160, 351, 271))
        self.settingGroupBpx.setStyleSheet("QGroupBox\n"
"{\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(166, 166, 166);\n"
"    border-style: none;\n"
"\n"
"}")
        self.settingGroupBpx.setAlignment(QtCore.Qt.AlignCenter)
        self.settingGroupBpx.setObjectName("settingGroupBpx")
        self.label_2 = QtWidgets.QLabel(self.settingGroupBpx)
        self.label_2.setGeometry(QtCore.QRect(26, 50, 62, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(61, 61, 61);\n"
"    background-color: rgb(166, 166, 166); \n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.settingGroupBpx)
        self.label_3.setGeometry(QtCore.QRect(26, 102, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("    background-color: rgb(166, 166, 166); \n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.settingGroupBpx)
        self.label_4.setGeometry(QtCore.QRect(26, 215, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("    background-color: rgb(166, 166, 166); \n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.settingGroupBpx)
        self.lineEdit.setGeometry(QtCore.QRect(130, 100, 201, 31))
        self.lineEdit.setStyleSheet("    background-color: rgb(255, 255, 255); \n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.settingGroupBpx)
        self.timeEdit.setGeometry(QtCore.QRect(130, 210, 171, 31))
        self.timeEdit.setStyleSheet("    background-color: rgb(255, 255, 255); \n"
"")
        self.timeEdit.setObjectName("timeEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.settingGroupBpx)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 50, 131, 31))
        self.lineEdit_2.setStyleSheet("    background-color: rgb(255, 255, 255); \n"
"    border-style: none;\n"
"")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.fontComboBox = QtWidgets.QFontComboBox(self.settingGroupBpx)
        self.fontComboBox.setGeometry(QtCore.QRect(131, 150, 161, 31))
        self.fontComboBox.setStyleSheet("    background-color: rgb(255, 255, 255); \n"
"")
        self.fontComboBox.setObjectName("fontComboBox")
        self.label_5 = QtWidgets.QLabel(self.settingGroupBpx)
        self.label_5.setGeometry(QtCore.QRect(26, 150, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("    background-color: rgb(166, 166, 166); \n"
"")
        self.label_5.setObjectName("label_5")
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.timeEdit.raise_()
        self.lineEdit_2.raise_()
        self.fontComboBox.raise_()
        self.label_5.raise_()
        self.lineEdit.raise_()
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 490, 121, 41))
        self.pushButton.setStyleSheet("    font-size: 30px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(166, 166, 166);\n"
"    border-style: none;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 490, 121, 41))
        self.pushButton_2.setStyleSheet("    font-size: 30px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(166, 166, 166);\n"
"    border-style: none;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.functionGroupBox.raise_()
        self.label.raise_()
        self.settingGroupBpx.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionversion = QtWidgets.QAction(MainWindow)
        self.actionversion.setObjectName("actionversion")
        self.actioncopy = QtWidgets.QAction(MainWindow)
        self.actioncopy.setObjectName("actioncopy")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionquit = QtWidgets.QAction(MainWindow)
        self.actionquit.setObjectName("actionquit")
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionpaste_data_only = QtWidgets.QAction(MainWindow)
        self.actionpaste_data_only.setObjectName("actionpaste_data_only")
        self.actionpaste_with_syosiki = QtWidgets.QAction(MainWindow)
        self.actionpaste_with_syosiki.setObjectName("actionpaste_with_syosiki")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sosei"))
        self.functionGroupBox.setTitle(_translate("MainWindow", "Function"))
        self.radioButton.setText(_translate("MainWindow", "heathy mode"))
        self.radioButton_3.setText(_translate("MainWindow", "nekoze mode"))
        self.radioButton_2.setText(_translate("MainWindow", "manner mode"))
        self.settingGroupBpx.setTitle(_translate("MainWindow", "Setting"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "E-mail"))
        self.label_4.setText(_translate("MainWindow", "Time"))
        self.label_5.setText(_translate("MainWindow", "Font"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Finish"))
        self.actionversion.setText(_translate("MainWindow", "version"))
        self.actioncopy.setText(_translate("MainWindow", "copy"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        self.actionquit.setText(_translate("MainWindow", "quit"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionnew.setStatusTip(_translate("MainWindow", "create a new action"))
        self.actionnew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionpaste_data_only.setText(_translate("MainWindow", "paste (data only)"))
        self.actionpaste_with_syosiki.setText(_translate("MainWindow", "paste( with syosiki)"))


import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
