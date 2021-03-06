# -*- coding: utf-8 -*-

import ntpath
import os
import os.path
import subprocess
# Form implementation generated from reading ui file 'dicta.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import threading
import tkinter as tk
from tkinter import filedialog

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize

from CpCode import CpCode
from JavaCode import JavaCode
from PythonCode import PythonCode
from SpeechToText import SpeechToText


class UiMainWindow(object):
    textEdit = None
    file_path = None
    speechToTextObject = SpeechToText()

    def setupUi(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(1400, 900)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 350, 811, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 50, 1370, 780))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1370, 780))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1370, 780))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setUndoRedoEnabled(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.saveFileButton = QtWidgets.QToolButton(self.centralwidget)
        self.saveFileButton.setGeometry(QtCore.QRect(100, 3, 40, 40))
        self.saveFileButton.setStatusTip("")
        program_path = self.presentworkingdirectory()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(program_path + "/icons/saveFile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveFileButton.setIcon(icon)
        self.saveFileButton.setIconSize(QSize(40, 40))
        self.saveFileButton.setObjectName("toolButton")
        self.saveFileButton.clicked.connect(self.save_file)

        # new button
        self.newFileButton = QtWidgets.QToolButton(self.centralwidget)
        self.newFileButton.setGeometry(QtCore.QRect(10, 3, 40, 40))
        self.newFileButton.setAcceptDrops(False)
        self.newFileButton.setStatusTip("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(program_path + "/icons/newFile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newFileButton.setIcon(icon1)
        self.newFileButton.setIconSize(QSize(40, 40))
        self.newFileButton.setObjectName("toolButton_2")
        self.newFileButton.clicked.connect(self.new_file)

        # build button
        self.compileButton = QtWidgets.QToolButton(self.centralwidget)
        self.compileButton.setGeometry(QtCore.QRect(255, 3, 40, 40))
        self.compileButton.setStatusTip("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(program_path + "/icons/compileFile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.compileButton.setIcon(icon2)
        self.compileButton.setIconSize(QSize(40, 40))
        self.compileButton.setObjectName("toolButton_3")
        self.compileButton.clicked.connect(self.compile)

        # open button
        self.openFileButton = QtWidgets.QToolButton(self.centralwidget)
        self.openFileButton.setGeometry(QtCore.QRect(55, 3, 40, 40))
        self.openFileButton.setAcceptDrops(False)
        self.openFileButton.setStatusTip("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(program_path + "/icons/openFile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openFileButton.setIcon(icon3)
        self.openFileButton.setIconSize(QSize(40, 40))
        self.openFileButton.setObjectName("toolButton_4")
        self.openFileButton.clicked.connect(self.open_file)

        # run button
        # self.executeButton = QtWidgets.QToolButton(self.centralwidget)
        # self.executeButton.setGeometry(QtCore.QRect(300, 3, 40, 40))
        # self.executeButton.setStatusTip("")
        # icon4 = QtGui.QIcon()
        # icon4.addPixmap(QtGui.QPixmap(program_path + "/icons/runFile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.executeButton.setIcon(icon4)
        # self.executeButton.setIconSize(QSize(40, 40))
        # self.executeButton.setObjectName("toolButton_5")
        # self.executeButton.clicked.connect(self.execute_java)
        # self.toolButton_5.clicked.connect(self.toolButton, self.fontPicker())

        # close button
        self.closeFileButton = QtWidgets.QToolButton(self.centralwidget)
        self.closeFileButton.setGeometry(QtCore.QRect(145, 3, 40, 40))
        self.closeFileButton.setStatusTip("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(program_path + "/icons/closeFile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeFileButton.setIcon(icon5)
        self.closeFileButton.setIconSize(QSize(40, 40))
        self.closeFileButton.setObjectName("toolButton_6")
        self.closeFileButton.clicked.connect(self.close_file)

        self.startButton = QtWidgets.QToolButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(500, 3, 91, 31))
        self.startButton.setStatusTip("")
        # icon7 = QtGui.QIcon()
        # icon7.addPixmap(QtGui.QPixmap(program_path + "/icons/save_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.toolButton7.setIcon(icon)
        self.startButton.setObjectName("toolButton7")
        # self.startButton.clicked.connect(self.start_listening)
        self.startButton.clicked.connect(self.threadListen)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        main_window.setMenuBar(self.menubar)
        # status bar
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        # setting text in status bar
        self.statusbar.showMessage("Welcome")
        main_window.setStatusBar(self.statusbar)
        # menu items
        self.actionNew = QtWidgets.QAction(main_window)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.setShortcut("Ctrl+N")
        self.actionNew.triggered.connect(self.new_file)

        self.actionOpen = QtWidgets.QAction(main_window)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.triggered.connect(self.open_file)

        self.actionSave = QtWidgets.QAction(main_window)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.triggered.connect(self.save_file)

        self.actionSave_As = QtWidgets.QAction(main_window)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.triggered.connect(self.saveAsFile)

        self.actionProperties = QtWidgets.QAction(main_window)
        self.actionProperties.setObjectName("actionProperties")

        self.actionQuit = QtWidgets.QAction(main_window)
        self.actionQuit.setObjectName("actionQuit")

        self.actionClose = QtWidgets.QAction(main_window)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.triggered.connect(self.close_file)

        self.actionUndo = QtWidgets.QAction(main_window)
        self.actionUndo.setObjectName("actionUndo")
        self.actionUndo.setShortcut("Ctrl+Z")
        self.actionUndo.triggered.connect(self.undo)

        self.actionRedo = QtWidgets.QAction(main_window)
        self.actionRedo.setObjectName("actionRedo")
        self.actionRedo.setShortcut("Ctrl+Y")
        self.actionRedo.triggered.connect(self.redo)

        '''self.actionFont = QtWidgets.QAction(MainWindow)
        self.actionFont.setObjectName("actionFont")
        #self.actionFont.triggered.connect(self.start_listening)
        '''
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionProperties)
        self.menuFile.addSeparator()

        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        # self.menuEdit.addAction(self.actionFont)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        self.MainWindow = main_window
        # QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL("clicked()"), self.fontPicker())

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Dicta Code"))
        program_path = self.presentworkingdirectory()
        icon1 = QtGui.QIcon()
        # mainwindow icon setting
        icon1.addPixmap(QtGui.QPixmap(program_path + "/icons/New_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon1)
        # self.label.setText(_translate("MainWindow", "Compiler:"))
        self.saveFileButton.setToolTip(_translate("MainWindow", "Save"))
        self.saveFileButton.setText(_translate("MainWindow", "..."))
        self.newFileButton.setToolTip(_translate("MainWindow", "New Class"))
        self.newFileButton.setText(_translate("MainWindow", "..."))
        self.compileButton.setToolTip(_translate("MainWindow", "Compile"))
        self.compileButton.setText(_translate("MainWindow", "..."))
        self.openFileButton.setToolTip(_translate("MainWindow", "Open File"))
        self.openFileButton.setText(_translate("MainWindow", "..."))
        # self.executeButton.setToolTip(_translate("MainWindow", "Run"))
        # self.executeButton.setText(_translate("MainWindow", "..."))
        self.closeFileButton.setToolTip(_translate("MainWindow", "Close File"))
        self.closeFileButton.setText(_translate("MainWindow", "..."))
        self.startButton.setText(_translate("MainWindow", "Start"))
        # self.toolButton8.setText(_translate("MainWindow", "Stop"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save "))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionProperties.setText(_translate("MainWindow", "Properties"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        # self.actionFont.setText(_translate("MainWindow", "Font"))

    # onclick functions for buttons

    def createConverter(self, fileType):
        print(fileType)
        if fileType == "java":
            self.converterObject = JavaCode()
        elif fileType == "cpp":
            self.converterObject = CpCode()
        else:
            self.converterObject = PythonCode()

    def new_file(self):

        root = tk.Tk()
        root.withdraw()
        self.file_path = filedialog.asksaveasfilename(title="New File", filetypes=[("Java File", "*.java"),
                                                                                   ("Python File", "*.py"),
                                                                                   ("Cpp File", "*.cpp")])
        if self.file_path:
            print(self.file_path)
            f = self.file_path
            fileName = ntpath.basename(self.file_path)
            print(fileName)
            self.createConverter(fileName[fileName.rindex(".") + 1:])
            print(fileName[0:fileName.rindex(".")])
            file1 = open(f, "w")
            if fileName[fileName.rindex(".") + 1:] == "java":
                x = """class """ + fileName[0:fileName.rindex(".")] + """
{
    public static void main(String args[])
    {
    
    }
    
}
"""
            elif fileName[fileName.rindex(".") + 1:] == "cpp":
                x = """#include <iostream>
using namespace std;

int main() 
{
    cout << "Hello, World!";
    return 0;
}
"""
            else:
                x = ""
            self.textEdit.setText(str(x))
            file1.close()
            self.statusbar.showMessage("File Created")

    def saveAsFile(self):
        root = tk.Tk()
        root.withdraw()
        f = filedialog.asksaveasfilename(title="SaveAs", filetypes=[("Java File", "*.java"),
                                                                    ("Python File", "*.py")])
        text = self.textEdit.toPlainText()
        # print(text)
        if f:
            file1 = open(f + ".java", "w")
            file1.write(text)
            file1.close()

    def save_file(self):
        text = self.textEdit.toPlainText()
        print(self.file_path)
        if self.file_path:
            fileAddress = self.file_path
            file = open(fileAddress, "w")
            file.write(text)
            file.close()
            t = ""
            file = open(fileAddress, "r")
            for x in file.readlines():
                print(x)
                t = t + x
            self.textEdit.setText(str(t))
            self.statusbar.showMessage("File Saved...")
            file.close()

        else:
            self.statusbar.showMessage("Please Open a file...")

    def close_file(self):
        text = self.textEdit.toPlainText()

        if self.file_path:
            f = self.file_path
            file1 = open(f, "w")
            # print("hello")
            file1.write(text)
            file1.close()
            self.statusbar.showMessage("File Closed")
        self.textEdit.setText("")

    def open_file(self):
        root = tk.Tk()
        root.withdraw()
        self.file_path = filedialog.askopenfilename(filetypes=[("Java File", "*.java"),
                                                               ("Python File", "*.py"),
                                                               ("Cpp File", "*.cpp")])

        t = ""
        if self.file_path:
            self.createConverter(self.file_path[self.file_path.rindex(".") + 1:])
            file1 = open(self.file_path, "r")
            for x in file1.readlines():
                print(x)
                t = t + x
            file1.close()
            self.statusbar.showMessage("File Opened")
        self.textEdit.setText(str(t))

    def undo(self):
        if self.textEdit:
            self.textEdit.undo()

    def redo(self):
        if self.textEdit:
            self.textEdit.redo()

    def compile(self, fileType):
        if fileType == "java":
            self.compile_java()
        elif fileType == "cpp":
            self.compile_java()
        else:
            self.compile_java()

    def compile_cpp(self):
        if self.file_path:
            cmd = 'g++ ' + self.file_path
            proc = subprocess.Popen(cmd, shell=True)
            self.statusbar.showMessage("File Compiled")
        else:
            self.statusbar.showMessage("please select a file to compile")

    def compile_python(self):
        if self.file_path:
            cmd = 'python ' + self.file_path
            proc = subprocess.Popen(cmd, shell=True)
            self.statusbar.showMessage("File Compiled")
        else:
            self.statusbar.showMessage("please select a file to compile")

    def compile_java(self):
        if self.file_path:
            cmd = 'javac ' + self.file_path
            proc = subprocess.Popen(cmd, shell=True)
            self.statusbar.showMessage("File Compiled")
        else:
            self.statusbar.showMessage("please select a file to compile")

    def execute_java(self):

        if self.file_path:
            java_class, ext = os.path.splitext(self.file_path)
            cmd = ['java', java_class + ".class"]
            print(cmd)
            subprocess.call(cmd, shell=True)
            self.statusbar.showMessage("File Executed")
        else:
            self.statusbar.showMessage("please select a file to run")

    @staticmethod
    def presentworkingdirectory():
        path = os.getcwd()
        return path

    def threadListen(self):
        thread = threading.Thread(target=self.start_listening)
        thread.start()

    def start_listening(self):
        self.statusbar.showMessage("Listening")
        self.speechToTextObject.listen()
        print(self.speechToTextObject.returnString())
        print(self.converterObject.optimizeInputString(self.speechToTextObject.returnString()))
        if self.speechToTextObject.returnString() == "noInternet":
            self.statusbar.showMessage("No Internet Connection")
        elif self.speechToTextObject.returnString() == "":
            self.statusbar.showMessage("Googe Speech Recognition could not understand audio")
        else:
            self.s = self.speechToTextObject.returnString()
            self.statusbar.showMessage("You Said: " + self.speechToTextObject.returnString())
            try:
                code = self.converterObject.convert(self.s)
            except:
                code = "error"
            self.textEdit.insertPlainText(code)

    def convert(self):
        print(self.converterObject.putString(self.s))

    def stop_listening(self):
        self.listening = False

    def changeRecording(self, value=1):
        self.speechToTextObject.recordingtime = value

    def changeSilentTime(self, value=1):
        self.speechToTextObject.silenttime = value

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
