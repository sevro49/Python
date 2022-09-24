# komut satırından çalıştırırsak sys modülü argümanlar vererek programı çalıştıracak.
import sys

from PyQt5 import QtWidgets, QtGui

# pyqt programlama içinde mutlaka bir uygulama objesi olmalıdır.


def Pencere():

    app = QtWidgets.QApplication(sys.argv)  # uygulama oluşturuldu
    pencere = QtWidgets.QWidget()  # pencere oluşturuyoruz

    pencere.setWindowTitle("PyQt5 Ders 1")  # pencere başlığı

    pencere.show()

    # çarpı tuşuna basmadığımız sürece uygulama çalışıyor. gerekli
    sys.exit(app.exec_())


Pencere()
