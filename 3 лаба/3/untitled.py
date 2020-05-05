# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import datetime
import re
import tkinter.messagebox
from itertools import groupby
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(619, 334)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 621, 301))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 619, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())


        self.statusBarLabel = QtWidgets.QLabel("")
        self.statusBarLabel1 = QtWidgets.QLabel("")

        self.statusBarLabel.setObjectName("statusBarLabel")
        self.statusBarLabel1.setObjectName("statusBarLabel1")
        self.statusbar.addPermanentWidget(self.statusBarLabel, 60)
        self.statusbar.addPermanentWidget(self.statusBarLabel1, 40)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Лог"))
        self.action.setText(_translate("MainWindow", "Открыть файл"))
        self.action_2.setText(_translate("MainWindow", "Экспорт"))
        self.action_3.setText(_translate("MainWindow", "Добавить в лог"))
        self.action_4.setText(_translate("MainWindow", "Просмотр"))

        self.action.triggered.connect(self.browse)
        self.action_2.triggered.connect(self.export)
        self.action_3.triggered.connect(self.addToLog)
        self.action_4.triggered.connect(self.showLog)
        self.text = ""
        self.logfilename = 'script18.log'
        self.checkLog()


    def checkLog(self):
        root = tkinter.Tk()
        root.withdraw()
        if not(os.path.exists(self.logfilename)):
            tkinter.messagebox.showinfo(title="Файл", message="Файл лога не найден. Файл будет создан автоматически")
            f = open(self.logfilename, 'w')
            f.close()
        root.destroy()

    def addToLog(self):
        file = open(self.logfilename, 'a')
        text = self.textEdit.toPlainText()+"\n"
        file.write(text)
        file.close()

    def export(self):
        fld = QtWidgets.QFileDialog()
        filename = fld.getSaveFileName(fld, 'Сохранить файл', "", 'Text files (*.txt);;All files (*.*)')
        if (filename[0] != "") :
            file = open(filename[0], 'w')
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()

    def showLog(self):
        root = tkinter.Tk()
        root.withdraw()
        if tkinter.messagebox.askyesno("Просмотр лога","Вы действительно хотите открыть лог? Данные последних поисков будут потеряны!") :
            with open(self.logfilename, 'r') as f:
                content = f.read()
            self.textEdit.setText(content)

    def browse(self):
        fld = QtWidgets.QFileDialog()
        filename = fld.getOpenFileName(fld, 'Выберите файл', "", 'Text files (*.txt);;All files (*.*)')
        with open(filename[0], 'r') as f:
            content = f.read()
        self.statusBarLabel.setText('Обработан файл: '+f.name)
        self.statusBarLabel1.setText(str(os.path.getsize(f.name))+" байт")
        self.text += "Файл "+f.name+" был обработан "+str(datetime.datetime.now())
        self.text += "\n\n"
        regexp = r'^\.'
        results = re.findall(r'(\(\d{3}\)\d{3}-\d{2}-\d{2})|(\(\d{3}\)\d{7})', content)
        res = []
        for result in results:
            if result[0] != "":
                res.append(result[0])
            elif result[1] != "":
                res.append(result[1])

        lines = content.split("\n")
        resultsIndx = []

        def f(ph):
            linenmb = 1
            for line in lines:
                char = line.find(ph)
                if char != -1:
                    self.text += "Строка " + str(linenmb) + ", позиция " + str(char) + ":" + "найдено" + ph+"\n"
                linenmb += 1

        res = [el for el, _ in groupby(res)]
        for phone in res:
            f(phone)

        self.textEdit.setText(self.text)
        self.text += "\n\n"



