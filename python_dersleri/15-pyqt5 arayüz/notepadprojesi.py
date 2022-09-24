import os
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QFileDialog, QAction, QMainWindow, qApp


class Notepad(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yaziAlani = QTextEdit()
        self.temizle = QPushButton("Temizle")
        self.ac = QPushButton("Dosya Aç")
        self.kaydet = QPushButton("Kaydet")

        hBox = QHBoxLayout()
        hBox.addWidget(self.temizle)
        hBox.addWidget(self.ac)
        hBox.addWidget(self.kaydet)

        vBox = QVBoxLayout()
        vBox.addWidget(self.yaziAlani)
        vBox.addLayout(hBox)

        self.setLayout(vBox)
        self.setWindowTitle("NotePad")
        self.temizle.clicked.connect(self.yaziyiTemizle)
        self.ac.clicked.connect(self.dosyaAc)
        self.kaydet.clicked.connect(self.dosyaKaydet)

    def yaziyiTemizle(self):
        self.yaziAlani.clear()

    def dosyaAc(self):
        dosyaIsmi = QFileDialog.getOpenFileName(
            self, "Dosya Aç", os.getenv("Desktop"))
        with open(dosyaIsmi[0], "r") as file:
            self.yaziAlani.setText(file.read())

    def dosyaKaydet(self):
        dosyaIsmi = QFileDialog.getSaveFileName(
            self, "Dosya Kaydet", os.getenv("Desktop"))
        with open(dosyaIsmi[0], "w") as file:
            file.write(self.yaziAlani.toPlainText())


class Menu (QMainWindow):
    def __init__(self):
        super().__init__()

        self.pencere = Notepad()
        self.setCentralWidget(self.pencere)

        self.menuleriOlustur()

    def menuleriOlustur(self):
        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")

        dosyaAc = QAction("Dosya Aç", self)
        dosyaAc.setShortcut("Ctrl+O")

        dosyaKaydet = QAction("Dosya Kaydet", self)
        dosyaKaydet.setShortcut("Ctrl+S")

        temizle = QAction("Dosyayı Temizle", self)
        temizle.setShortcut("Ctrl+D")

        cikis = QAction("Çıkış", self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosyaAc)
        dosya.addAction(dosyaKaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response)

        self.setWindowTitle("Metin editörü")
        self.show()

    def response(self, action):
        if action.text() == "Dosya Aç":
            self.pencere.dosyaAc()
        elif action.text() == "Dosya Kaydet":
            self.pencere.dosyaKaydet()
        elif action.text() == "Dosyayı Temizle":
            self.pencere.yaziyiTemizle()
        elif action.text() == "Çıkış":
            qApp.quit()


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())
