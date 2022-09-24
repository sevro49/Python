from email.charset import QP
from filecmp import clear_cache
import os
import sys
from PyQt5.QtWidgets import QWidget, QApplication, qApp, QHBoxLayout, QVBoxLayout, QFileDialog, QTextEdit, QPushButton, QMainWindow, QAction


class Notepad(QWidget):

    def __init__(self):

        super().__init__()

        self.ui()

    def ui(self):

        self.textEdit = QTextEdit()
        self.open = QPushButton("Open")
        self.save = QPushButton("Save")
        self.clear = QPushButton("Clear")

        hBox = QHBoxLayout()
        hBox.addWidget(self.open)
        hBox.addWidget(self.save)
        hBox.addWidget(self.clear)

        vBox = QVBoxLayout()
        vBox.addWidget(self.textEdit)
        vBox.addLayout(hBox)

        self.setLayout(vBox)

        self.open.clicked.connect(self.openFile)
        self.save.clicked.connect(self.saveFile)
        self.clear.clicked.connect(self.clearTextEdit)

    def openFile(self):
        fileName = QFileDialog.getOpenFileName(
            self, "Open", os.getenv("Desktop"))
        with open(fileName[0], "r") as file:
            self.textEdit.setText(file.read())

    def saveFile(self):
        fileName = QFileDialog.getSaveFileName(
            self, "Save", os.getenv("Desktop"))
        with open(fileName[0], "w") as file:
            file.write(self.textEdit.toPlainText())

    def clearTextEdit(self):
        self.textEdit.clear()


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

        self.window = Notepad()
        self.setCentralWidget(self.window)

        self.createMenu()

    def createMenu(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")

        openFile = QAction("Open File", self)
        openFile.setShortcut("Ctrl+O")

        saveFile = QAction("Save File", self)
        saveFile.setShortcut("Ctrl+S")

        clear = QAction("Clear", self)
        clear.setShortcut("Ctrl+D")

        quit = QAction("Quit", self)
        quit.setShortcut("Ctrl+Q")

        file.addAction(openFile)
        file.addAction(saveFile)
        file.addAction(clear)
        file.addAction(quit)
        file.triggered.connect(self.response)

        self.setGeometry(450, 150, 500, 500)
        self.show()

    def response(self, action):

        if action.text() == "Open File":
            self.window.openFile()

        elif action.text() == "Save File":
            self.window.saveFile()

        elif action.text() == "Clear":
            self.window.clearTextEdit()

        elif action.text() == "Quit":
            qApp.quit()


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())
