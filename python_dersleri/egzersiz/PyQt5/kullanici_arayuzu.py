import sys
import sqlite3

from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        self.baglantiOlustur()
        self.init_ui()

    def baglantiOlustur(self):
        # yoksa database oluşturacak, varsa bağlanacak
        baglanti = sqlite3.connect(
            "C:/Users/emreg/Desktop/EMRE/YAZILIM/PYTHON/PYTHON_dosyalari/python_dersleri/egzersiz/PyQt5/database.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute(
            "Create Table If not exists üyeler (kullaniciAdi TEXT, parola TEXT)")
        baglanti.commit()

    def init_ui(self):
        self.kullaniciAdi = QtWidgets.QLineEdit()
        self.kullaniciAdi.setPlaceholderText("Kullanıcı Adı")
        self.parola = QtWidgets.QLineEdit()
        # parolanın yıldız gibi görünmesini sağlar
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.parola.setPlaceholderText("Parola")
        self.giris = QtWidgets.QPushButton("Giriş")
        self.yaziAlani = QtWidgets.QLabel("")

        vBox = QtWidgets.QVBoxLayout()
        vBox.addWidget(self.kullaniciAdi)
        vBox.addWidget(self.parola)
        vBox.addWidget(self.yaziAlani)
        vBox.addStretch()
        vBox.addWidget(self.giris)

        hBox = QtWidgets.QHBoxLayout()
        hBox.addStretch()
        hBox.addLayout(vBox)
        hBox.addStretch()

        self.setLayout(hBox)
        self.setWindowTitle("Kullanıcı girişi")
        self.giris.clicked.connect(self.login)
        self.show()

    def login(self):
        adi = self.kullaniciAdi.text()
        par = self.parola.text()
        self.cursor.execute(
            "Select * From üyeler where kullaniciAdi = ? and parola = ?", (adi, par))
        data = self.cursor.fetchall()

        if(len(data) == 0):  # eğer hiçbir veri getirilmiyorsa len = 0 olur. O yüzden len kullandık
            self.yaziAlani.setText(
                "Böyle bir kullanıcı yok\nLütfen tekrar deneyin")
        else:
            self.yaziAlani.setText("Hoş geldiniz " + adi)


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
