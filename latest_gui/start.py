# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/cat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
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
        self.programNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.programNameLabel.setGeometry(QtCore.QRect(230, 20, 341, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(72)
        self.programNameLabel.setFont(font)
        self.programNameLabel.setObjectName("programNameLabel")
        self.functionGBox = QtWidgets.QGroupBox(self.centralwidget)
        self.functionGBox.setGeometry(QtCore.QRect(30, 160, 341, 271))
        self.functionGBox.setAutoFillBackground(False)
        self.functionGBox.setStyleSheet("QGroupBox\n"
"{\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(166, 166, 166);\n"
"    border-style: none;\n"
"    padding-top: 10px;\n"
"}")
        self.functionGBox.setAlignment(QtCore.Qt.AlignCenter)
        self.functionGBox.setObjectName("functionGBox")
        self.healthyModeBtn = QtWidgets.QRadioButton(self.functionGBox)
        self.healthyModeBtn.setGeometry(QtCore.QRect(22, 65, 180, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.healthyModeBtn.setFont(font)
        self.healthyModeBtn.setStyleSheet("    background-color: rgb(166, 166, 166); \n"
"")
        self.healthyModeBtn.setObjectName("healthyModeBtn")
        self.mannerModeBtn = QtWidgets.QRadioButton(self.functionGBox)
        self.mannerModeBtn.setGeometry(QtCore.QRect(22, 115, 180, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mannerModeBtn.setFont(font)
        self.mannerModeBtn.setStyleSheet("    background-color: rgb(166, 166, 166); \n"
"")
        self.mannerModeBtn.setObjectName("mannerModeBtn")
        self.nekozeModeBtn = QtWidgets.QRadioButton(self.functionGBox)
        self.nekozeModeBtn.setGeometry(QtCore.QRect(22, 165, 180, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.nekozeModeBtn.setFont(font)
        self.nekozeModeBtn.setStyleSheet("    background-color: rgb(166, 166, 166); \n"
"")
        self.nekozeModeBtn.setObjectName("nekozeModeBtn")
        self.settingGBpx = QtWidgets.QGroupBox(self.centralwidget)
        self.settingGBpx.setGeometry(QtCore.QRect(420, 160, 351, 271))
        self.settingGBpx.setStyleSheet("QGroupBox\n"
"{\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(166, 166, 166);\n"
"    border-style: none;\n"
"\n"
"}")
        self.settingGBpx.setAlignment(QtCore.Qt.AlignCenter)
        self.settingGBpx.setObjectName("settingGBpx")
        self.nameLabel = QtWidgets.QLabel(self.settingGBpx)
        self.nameLabel.setGeometry(QtCore.QRect(26, 50, 62, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet("color: rgb(61, 61, 61);\n"
"    background-color: rgb(166, 166, 166); \n"
"")
        self.nameLabel.setObjectName("nameLabel")
        self.emailLabel = QtWidgets.QLabel(self.settingGBpx)
        self.emailLabel.setGeometry(QtCore.QRect(26, 102, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.emailLabel.setFont(font)
        self.emailLabel.setAutoFillBackground(False)
        self.emailLabel.setStyleSheet("    background-color: rgb(166, 166, 166); \n"
"")
        self.emailLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.emailLabel.setObjectName("emailLabel")
        self.timeLabel = QtWidgets.QLabel(self.settingGBpx)
        self.timeLabel.setGeometry(QtCore.QRect(30, 210, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("    background-color: rgb(166, 166, 166); \n"
"")
        self.timeLabel.setObjectName("timeLabel")
        self.emailEdit = QtWidgets.QLineEdit(self.settingGBpx)
        self.emailEdit.setGeometry(QtCore.QRect(130, 100, 171, 31))
        self.emailEdit.setStyleSheet("    background-color: rgb(255, 255, 255); \n"
"")
        self.emailEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.emailEdit.setObjectName("emailEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.settingGBpx)
        self.timeEdit.setGeometry(QtCore.QRect(130, 200, 171, 31))
        self.timeEdit.setStyleSheet("    background-color: rgb(255, 255, 255); \n"
"")
        self.timeEdit.setObjectName("timeEdit")
        self.nameEdit = QtWidgets.QLineEdit(self.settingGBpx)
        self.nameEdit.setGeometry(QtCore.QRect(130, 50, 171, 31))
        self.nameEdit.setStyleSheet("    background-color: rgb(255, 255, 255); \n"
"    border-style: none;\n"
"")
        self.nameEdit.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.nameEdit.setObjectName("nameEdit")
        self.fontComboBox = QtWidgets.QFontComboBox(self.settingGBpx)
        self.fontComboBox.setGeometry(QtCore.QRect(131, 150, 171, 31))
        self.fontComboBox.setStyleSheet("    background-color: rgb(255, 255, 255); \n"
"")
        self.fontComboBox.setObjectName("fontComboBox")
        self.fontLabel = QtWidgets.QLabel(self.settingGBpx)
        self.fontLabel.setGeometry(QtCore.QRect(26, 150, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fontLabel.setFont(font)
        self.fontLabel.setStyleSheet("    background-color: rgb(166, 166, 166); \n"
"")
        self.fontLabel.setObjectName("fontLabel")
        self.nameLabel.raise_()
        self.emailLabel.raise_()
        self.timeLabel.raise_()
        self.timeEdit.raise_()
        self.nameEdit.raise_()
        self.fontComboBox.raise_()
        self.fontLabel.raise_()
        self.emailEdit.raise_()
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(210, 460, 161, 61))
        self.startBtn.setStyleSheet("    font-size: 30px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(166, 166, 166);\n"
"    border-style: none;")
        self.startBtn.setObjectName("startBtn")
        self.finishBtn = QtWidgets.QPushButton(self.centralwidget)
        self.finishBtn.setGeometry(QtCore.QRect(420, 460, 151, 61))
        self.finishBtn.setStyleSheet("    font-size: 30px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(166, 166, 166);\n"
"    border-style: none;")
        self.finishBtn.setObjectName("finishBtn")
        self.functionGBox.raise_()
        self.programNameLabel.raise_()
        self.settingGBpx.raise_()
        self.startBtn.raise_()
        self.finishBtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuAbout_Program = QtWidgets.QMenu(self.menuBar)
        self.menuAbout_Program.setObjectName("menuAbout_Program")
        MainWindow.setMenuBar(self.menuBar)
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
        self.menuBar.addAction(self.menuAbout_Program.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.programNameLabel.setText(_translate("MainWindow", "SOSEI"))
        self.functionGBox.setTitle(_translate("MainWindow", "Function"))
        self.healthyModeBtn.setText(_translate("MainWindow", "heathy mode"))
        self.mannerModeBtn.setText(_translate("MainWindow", "nekoze mode"))
        self.nekozeModeBtn.setText(_translate("MainWindow", "manner mode"))
        self.settingGBpx.setTitle(_translate("MainWindow", "Setting"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.emailLabel.setText(_translate("MainWindow", "E-mail"))
        self.timeLabel.setText(_translate("MainWindow", "Time"))
        self.fontLabel.setText(_translate("MainWindow", "Font"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.finishBtn.setText(_translate("MainWindow", "Finish"))
        self.menuAbout_Program.setTitle(_translate("MainWindow", "About Program"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
