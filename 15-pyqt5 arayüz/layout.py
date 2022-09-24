# komut satırından çalıştırırsak sys modülü argümanlar vererek programı çalıştıracak.
import sys
from winreg import OpenKey

from PyQt5 import QtWidgets, QtGui

# pyqt programlama içinde mutlaka bir uygulama objesi olmalıdır.


def Pencere():

    app = QtWidgets.QApplication(sys.argv)  # uygulama oluşturuldu

    pencere = QtWidgets.QWidget()  # pencere oluşturuyoruz
    pencere.setWindowTitle("PyQt5 Ders 1")  # pencere başlığı
    pencere.setGeometry(100, 200, 500, 500)  # x, y, genişlik, yükseklik

    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")

    """ h_box = QtWidgets.QHBoxLayout()
    # h_box.addStretch() # buradan sonra boşluk koyar
    h_box.addWidget(okay)
    # h_box.addStretch() # buradan sonra boşluk koyar
    h_box.addWidget(cancel)
    h_box.addStretch()  # buradan sonra boşluk koyar
    pencere.setLayout(h_box)"""

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    
    

    pencere.setLayout(v_box)
    pencere.show()

    # çarpı tuşuna basmadığımız sürece uygulama çalışıyor. gerekli
    sys.exit(app.exec_())


Pencere()
