# komut satırından çalıştırırsak sys modülü argümanlar vererek programı çalıştıracak.
import sys

from PyQt5 import QtWidgets, QtGui

# pyqt programlama içinde mutlaka bir uygulama objesi olmalıdır.


def Pencere():

    app = QtWidgets.QApplication(sys.argv)  # uygulama oluşturuldu
    pencere = QtWidgets.QWidget()  # pencere oluşturuyoruz

    pencere.setWindowTitle("PyQt5 Ders 1")  # pencere başlığı

    # etiket oluşturup pencere üzerine yapıştırıyoruz
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("Bu bir yazıdır.")  # etiket içine yazı ekliyoruz.
    etiket1.move(220, 40)  # etiketimizi taşıyoruz.

    # etiket2 oluşturup pencere üzerine yapıştırıyoruz.
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("49.png"))  # resim ekliyoruz
    etiket2.move(180, 70)

    pencere.setGeometry(100, 200, 500, 500)  # x, y, genişlik, yükseklik
    pencere.show()

    # çarpı tuşuna basmadığımız sürece uygulama çalışıyor. gerekli
    sys.exit(app.exec_())


Pencere()
