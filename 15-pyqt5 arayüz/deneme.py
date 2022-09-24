import os
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog


class Notepad(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yaziAlani = QTextEdit()
        self.ac = QPushButton("Dosya Aç")
        self.kaydet = QPushButton("Kaydet")
        self.temizle = QPushButton("Temizle")

        hBox = QHBoxLayout()
        hBox.addWidget(self.temizle)
        hBox.addWidget(self.ac)
        hBox.addWidget(self.kaydet)

        vBox = QVBoxLayout()
        vBox.addWidget(self.yaziAlani)
        vBox.addLayout(hBox)

        self.setLayout(vBox)
        self.temizle.clicked.connect(self.yaziTemizle)
        self.ac.clicked.connect(self.dosyaAc)
        self.kaydet.clicked.connect(self.dosyaKaydet)
        self.show()

    def yaziTemizle(self):
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

app = QApplication(sys.argv)
notepad = Notepad()
sys.exit(app.exec_())
