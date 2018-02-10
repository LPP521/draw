# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draw.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(281, 374)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(281, 374))
        MainWindow.setMaximumSize(QtCore.QSize(281, 374))
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setKerning(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(159, 112, 115, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.roll_label = QtWidgets.QLabel(self.centralwidget)
        self.roll_label.setGeometry(QtCore.QRect(15, 15, 253, 58))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.roll_label.setFont(font)
        self.roll_label.setAutoFillBackground(False)
        self.roll_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roll_label.setAlignment(QtCore.Qt.AlignCenter)
        self.roll_label.setWordWrap(False)
        self.roll_label.setObjectName("roll_label")
        self.remain_label = QtWidgets.QLabel(self.centralwidget)
        self.remain_label.setGeometry(QtCore.QRect(160, 214, 91, 16))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.remain_label.setFont(font)
        self.remain_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remain_label.setMouseTracking(False)
        self.remain_label.setObjectName("remain_label")
        self.selected_list = QtWidgets.QListWidget(self.centralwidget)
        self.selected_list.setGeometry(QtCore.QRect(15, 113, 139, 229))
        self.selected_list.setObjectName("selected_list")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 93, 54, 12))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.next_round = QtWidgets.QPushButton(self.centralwidget)
        self.next_round.setGeometry(QtCore.QRect(160, 182, 49, 23))
        self.next_round.setObjectName("next_round")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 281, 21))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        MainWindow.setMenuBar(self.menubar)
        self.open_file_action = QtWidgets.QAction(MainWindow)
        self.open_file_action.setObjectName("open_file_action")
        self.file_menu.addAction(self.open_file_action)
        self.menubar.addAction(self.file_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "开始"))
        self.roll_label.setText(_translate("MainWindow", "???"))
        self.remain_label.setText(_translate("MainWindow", "剩余人数："))
        self.label.setText(_translate("MainWindow", "已选"))
        self.next_round.setText(_translate("MainWindow", "新一轮"))
        self.file_menu.setTitle(_translate("MainWindow", "文件"))
        self.open_file_action.setText(_translate("MainWindow", "打开列表"))

