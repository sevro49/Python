import sys
from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow 


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()  # QMainWindow fonksiyonunun __init__() fonksiyonu

        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")

        dosyaAc = QAction("Dosya Aç", self)

        dosyaAc.setShortcut("Ctrl+O") # arada boşluk olmayacak şekilde yaz yoksa çalışmaz.

        dosyaKaydet = QAction("Dosya Kaydet", self)
        dosyaKaydet.setShortcut("Ctrl+S")

        cikis = QAction("Çıkış", self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosyaAc)
        dosya.addAction(dosyaKaydet)
        dosya.addAction(cikis)

        ara_ve_degistir = duzenle.addMenu("Ara ve Değiştir")
        ara = QAction("Ara", self)
        degistir = QAction("Değiştir", self)
        temizle = QAction("Temizle", self)
        ara_ve_degistir.addAction(ara)
        ara_ve_degistir.addAction(degistir)

        duzenle.addAction(temizle)

        # action a fonkisyonel özellik ekleme
        cikis.triggered.connect(self.cikisYap)

        # bir menü içinden hangi action a basıldığını anlama, python kendi içinde bir action objesi gönderdiği için bizim fonksiyona eklememiz gerekiyor
        dosya.triggered.connect(self.response)

        self.setWindowTitle("Menüler")
        self.show()

    def cikisYap(self):
        qApp.quit()

    # hangi action un basıldığını anlamak için içine parametre gönderiyoruz.
    def response(self, action):
        if action.text() == "Dosya Aç":
            print("Dosya Aç'a basıldı.")
        elif action.text() == "Dosya Kaydet":
            print("Dosya Kaydet'e basıldı.")
        elif action.text() == "Çıkış":
            print("Çıkış'a basıldı.")


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())
