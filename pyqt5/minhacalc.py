# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minhacalc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 338)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(211, 211, 211);\n"
"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 238);\n"
"background-color: rgb(222, 222, 222);")
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(10, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(70, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(130, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.btn3.setObjectName("btn3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 280, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 280, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(10, 160, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn4.setFont(font)
        self.btn4.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.btn4.setObjectName("btn4")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(130, 160, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn6.setFont(font)
        self.btn6.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.btn6.setObjectName("btn6")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(70, 160, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn5.setFont(font)
        self.btn5.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.btn5.setObjectName("btn5")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(10, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn7.setFont(font)
        self.btn7.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.btn7.setObjectName("btn7")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(130, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn9.setFont(font)
        self.btn9.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.btn9.setObjectName("btn9")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(70, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn8.setFont(font)
        self.btn8.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.btn8.setObjectName("btn8")
        self.btnmult = QtWidgets.QPushButton(self.centralwidget)
        self.btnmult.setGeometry(QtCore.QRect(190, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnmult.setFont(font)
        self.btnmult.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.btnmult.setObjectName("btnmult")
        self.btnmais = QtWidgets.QPushButton(self.centralwidget)
        self.btnmais.setGeometry(QtCore.QRect(190, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnmais.setFont(font)
        self.btnmais.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.btnmais.setObjectName("btnmais")
        self.btnmenos = QtWidgets.QPushButton(self.centralwidget)
        self.btnmenos.setGeometry(QtCore.QRect(190, 160, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnmenos.setFont(font)
        self.btnmenos.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.btnmenos.setObjectName("btnmenos")
        self.btnc = QtWidgets.QPushButton(self.centralwidget)
        self.btnc.setGeometry(QtCore.QRect(250, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnc.setFont(font)
        self.btnc.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);\n"
"")
        self.btnc.setObjectName("btnc")
        self.btnback = QtWidgets.QPushButton(self.centralwidget)
        self.btnback.setGeometry(QtCore.QRect(250, 160, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnback.setFont(font)
        self.btnback.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 0);\n"
"")
        self.btnback.setObjectName("btnback")
        self.btndiv = QtWidgets.QPushButton(self.centralwidget)
        self.btndiv.setGeometry(QtCore.QRect(250, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btndiv.setFont(font)
        self.btndiv.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.btndiv.setObjectName("btndiv")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(130, 280, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("background-color: rgb(44, 135, 255);\n"
"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_19.setObjectName("pushButton_19")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.pushButton_5.setText(_translate("MainWindow", "."))
        self.pushButton_6.setText(_translate("MainWindow", "0"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btnmult.setText(_translate("MainWindow", "*"))
        self.btnmais.setText(_translate("MainWindow", "+"))
        self.btnmenos.setText(_translate("MainWindow", "-"))
        self.btnc.setText(_translate("MainWindow", "C"))
        self.btnback.setText(_translate("MainWindow", "<|"))
        self.btndiv.setText(_translate("MainWindow", "/"))
        self.pushButton_19.setText(_translate("MainWindow", "="))
