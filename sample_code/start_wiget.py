# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_wiget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        """
        （１）オブジェクトへの着色
        background-colorの着色の仕方
        spring green #00FF7F
        参考：https://code.tiblab.net/python/pyqt/window_color
        """
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtGui.QColor('#00FF7F'))
        palette.setColor(QtGui.QPalette.Foreground, QtGui.QColor('#708090'))
        MainWindow.setPalette(palette)
        """
        （１）end
        """
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 321, 151))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.functionGroupBox = QtWidgets.QFrame(self.centralwidget)
        self.functionGroupBox.setGeometry(QtCore.QRect(100, 160, 231, 231))
        self.functionGroupBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.functionGroupBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.functionGroupBox.setLineWidth(3)
        self.functionGroupBox.setObjectName("functionGroupBox")

        self.radioButton = QtWidgets.QRadioButton(self.functionGroupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 180, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.functionGroupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 60, 180, 21))
        font = QtGui.QFont()
        font.setPointSize(14)


        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.functionGroupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 110, 180, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.settingGroupBpx = QtWidgets.QFrame(self.centralwidget)
        self.settingGroupBpx.setGeometry(QtCore.QRect(420, 150, 301, 281))
        self.settingGroupBpx.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settingGroupBpx.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settingGroupBpx.setLineWidth(3)
        self.settingGroupBpx.setObjectName("settingGroupBpx")
        self.setting_3 = QtWidgets.QFrame(self.settingGroupBpx)
        self.setting_3.setGeometry(QtCore.QRect(120, 230, 231, 231))
        self.setting_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setting_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setting_3.setLineWidth(3)
        self.setting_3.setObjectName("setting_3")
        self.label_2 = QtWidgets.QLabel(self.settingGroupBpx)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 62, 15))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.settingGroupBpx)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.settingGroupBpx)
        self.label_4.setGeometry(QtCore.QRect(30, 215, 62, 15))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.settingGroupBpx)
        self.lineEdit.setGeometry(QtCore.QRect(50, 120, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.settingGroupBpx)
        self.timeEdit.setGeometry(QtCore.QRect(50, 247, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.settingGroupBpx)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 60, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.fontComboBox = QtWidgets.QFontComboBox(self.settingGroupBpx)
        self.fontComboBox.setGeometry(QtCore.QRect(50, 180, 151, 21))
        self.fontComboBox.setObjectName("fontComboBox")
        self.label_5 = QtWidgets.QLabel(self.settingGroupBpx)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 62, 15))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 480, 121, 41))
        self.pushButton.setObjectName("pushButton")
        """
        （２）
        参考：https://stackoverflow.com/questions/20668060/pyqt-qpushbutton-background-color
        CSSのように色を変えることができる
        """
        self.pushButton.setStyleSheet("font-weight:bold;background-color: #708090; color: #FFFFFF")
        """
        （２）
        """
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 480, 121, 41))
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
        self.radioButton.setText(_translate("MainWindow", "heathy mode"))
        self.radioButton_3.setText(_translate("MainWindow", "nekoze mode"))
        self.radioButton_2.setText(_translate("MainWindow", "manner mode"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
