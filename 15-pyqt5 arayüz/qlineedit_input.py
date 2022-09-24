import sys
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()  # Qwidget sınıfının init() fonksiyonu
        self.init_ui()

    def init_ui(self):
        self.yaziAlani = QtWidgets.QLineEdit()  # yazı yazılabilen bir alan
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdir = QtWidgets.QPushButton("Yazdır")

        vBox = QtWidgets.QVBoxLayout()
        vBox.addWidget(self.yaziAlani)
        vBox.addWidget(self.temizle)
        vBox.addWidget(self.yazdir)
        vBox.addStretch()

        self.setLayout(vBox)
        self.temizle.clicked.connect(self.click)
        self.yazdir.clicked.connect(self.click)
        self.show()

    def click(self):
        sender = self.sender()  # hangi butona basıldığını anlamaya yarar.

        if sender.text() == "Temizle":  # buton üzerinde yazan yazıya göre karar verdi.
            self.yaziAlani.clear()
        else:
            print(self.yaziAlani.text())


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
