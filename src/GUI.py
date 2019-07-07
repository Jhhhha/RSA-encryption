# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy
from RSA import *

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.p = 0
        self.q = 0
        self.n = 0
        self.n1 = 0
        self.e = 0
        self.d = 0
        # self.work = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(718, 556)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.public_key_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.public_key_2.setGeometry(QtCore.QRect(70, 20, 471, 21))
        self.public_key_2.setObjectName("public_key_2")
        self.privat_key = QtWidgets.QLineEdit(self.centralWidget)
        self.privat_key.setGeometry(QtCore.QRect(70, 50, 471, 21))
        self.privat_key.setMouseTracking(False)
        self.privat_key.setObjectName("privat_key")
        self.public_key = QtWidgets.QLabel(self.centralWidget)
        self.public_key.setGeometry(QtCore.QRect(20, 20, 26, 19))
        self.public_key.setObjectName("public_key")
        self.private_key = QtWidgets.QLabel(self.centralWidget)
        self.private_key.setGeometry(QtCore.QRect(20, 80, 31, 16))
        self.private_key.setObjectName("private_key")
        self.gen_key = QtWidgets.QPushButton(self.centralWidget)
        self.gen_key.setGeometry(QtCore.QRect(560, 20, 141, 81))
        self.gen_key.setObjectName("gen_key")
        self.inputText = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.inputText.setGeometry(QtCore.QRect(70, 120, 631, 161))
        self.inputText.setObjectName("inputText")
        self.outputText = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.outputText.setGeometry(QtCore.QRect(70, 320, 631, 161))
        self.outputText.setObjectName("outputText")
        self.input = QtWidgets.QLabel(self.centralWidget)
        self.input.setGeometry(QtCore.QRect(20, 120, 31, 16))
        self.input.setObjectName("input")
        self.output = QtWidgets.QLabel(self.centralWidget)
        self.output.setGeometry(QtCore.QRect(20, 320, 31, 16))
        self.output.setObjectName("output")
        self.encrypt = QtWidgets.QPushButton(self.centralWidget)
        self.encrypt.setGeometry(QtCore.QRect(190, 285, 114, 32))
        self.encrypt.setObjectName("encrypt")
        self.decrypt = QtWidgets.QPushButton(self.centralWidget)
        self.decrypt.setGeometry(QtCore.QRect(420, 285, 114, 32))
        self.decrypt.setObjectName("decrypt")
        self.public_key_3 = QtWidgets.QLabel(self.centralWidget)
        self.public_key_3.setGeometry(QtCore.QRect(55, 20, 16, 19))
        self.public_key_3.setObjectName("public_key_3")
        self.public_key_4 = QtWidgets.QLabel(self.centralWidget)
        self.public_key_4.setGeometry(QtCore.QRect(54, 50, 16, 19))
        self.public_key_4.setObjectName("public_key_4")
        self.privat_key_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.privat_key_2.setGeometry(QtCore.QRect(70, 80, 471, 21))
        self.privat_key_2.setMouseTracking(False)
        self.privat_key_2.setObjectName("privat_key_2")
        self.public_key_5 = QtWidgets.QLabel(self.centralWidget)
        self.public_key_5.setGeometry(QtCore.QRect(55, 80, 16, 19))
        self.public_key_5.setObjectName("public_key_5")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 718, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.clickEvents()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA加密"))
        self.public_key.setText(_translate("MainWindow", "公钥"))
        self.private_key.setText(_translate("MainWindow", "私钥"))
        self.gen_key.setText(_translate("MainWindow", "随机生成"))
        self.input.setText(_translate("MainWindow", "输入"))
        self.output.setText(_translate("MainWindow", "输出"))
        self.encrypt.setText(_translate("MainWindow", "加密"))
        self.decrypt.setText(_translate("MainWindow", "解密"))
        self.public_key_3.setText(_translate("MainWindow", "N"))
        self.public_key_4.setText(_translate("MainWindow", "E"))
        self.public_key_5.setText(_translate("MainWindow", "D"))

    def Gen_keys(self):
        bit = 512
        self.p = getPrime(bit)
        self.q = getPrime(bit)

        print("p:", self.p)
        print("q:", self.q)
        self.n = self.p*self.q
        print("n:", self.n)

        self.e, self.d = getKeys(self.p, self.q, 32)
        self.public_key_2.setText(hex(self.n))
        # self.public_key_2.displayText()

        self.n1 = (self.p - 1) * (self.q - 1)

        self.privat_key.setText(hex(self.e))
        # self.privat_key.displayText()
        self.privat_key_2.setText(hex(self.d))
        # self.privat_key_2.displayText()
        print("e:", self.e)
        print("d:", self.d)

    # ﻿密码学真是一门有意思的学科！！！叶广智是一个弟弟！！！密码学真是一门有意思的学科！！！叶广智是一个弟弟！！！密码学真是一门有意思的学科！！！叶广智是一个弟弟！！！密码学真是一门有意思的学科！！！叶广智是一个弟弟！！！密码学真是一门有意思的学科！！！叶广智是一个弟弟！！！密码学真是一门有意思的学科！！！叶广智是一个弟弟！！！
    def E(self):
        self.e = bytes2ints_(self.privat_key.text())[0]
        self.n = bytes2ints_(self.public_key_2.text())[0]

        M = self.inputText.toPlainText()
        print("M" , M)
        P = encrypt(M, self.e, self.n, 64)
        self.outputText.setPlainText(P)
        print(P)
        # M_ = decrypt(P,d,n,8)
        # print(M_)


    def D(self):
        self.d = bytes2ints_(self.privat_key_2.text())[0]
        self.n = bytes2ints_(self.public_key_2.text())[0]

        S = self.inputText.toPlainText()
        print("S", S)
        # print("lol", decrypt(S, self.d, self.n, 512))
        self.outputText.setPlainText(decrypt(S, self.d, self.n, 64))

    def clickEvents(self):
        self.gen_key.clicked.connect(self.Gen_keys)
        self.encrypt.clicked.connect(self.E)
        self.decrypt.clicked.connect(self.D)



import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    new = Ui_MainWindow()
    new.show()
    print("H")
    sys.exit(app.exec_())

    # bit = 512
    # p = getPrime(bit)
    # print("p:",p)
    #
    # q = getPrime(bit)
    # print("q:", q)
    # #
    # n = p * q
    # print("n:", n)
    #
    # n1 = (p-1)*(q-1)
    # print("n1:", n1)
    #
    # p = 16137268290371297291
    # q = 14976755623516613029
    # n = 241683923616014646512063284721163004439
    # n1 = 241683923616014646480949260807275094120
    #
    # e, d = getKeys(p,q,32)
    # print("e:", e)
    # print("d:", d)
    #
    # str_ = "叶广智叶广3123智叶广智叶广智叶广3123智叶广智叶广智叶广3123智叶广智叶广智叶广3123智叶广智"
    # print("明文是：", str_)
    #
    # p = encrypt(str_, e, n, 8)
    # print("加密后：", p)
    #
    # m = decrypt(p, d, n ,8)
    # print("解密后：", m)
