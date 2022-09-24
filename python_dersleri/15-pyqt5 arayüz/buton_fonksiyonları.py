import sys
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget): # bu sınıftan fonksiyon alabiliyoruz

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yaziAlani = QtWidgets.QLabel("Bana henüz tıklanmadı")
        self.buton = QtWidgets.QPushButton("Bana tıkla")
        self.say = 0

        vBox = QtWidgets.QVBoxLayout()
        vBox.addWidget(self.buton)
        vBox.addWidget(self.yaziAlani)
        vBox.addStretch()

        hBox = QtWidgets.QHBoxLayout()
        hBox.addStretch()
        hBox.addLayout(vBox)
        hBox.addStretch()

        self.setLayout(hBox)  # buradaki self Pencere objesini ifade eder.
        self.buton.clicked.connect(self.click)
        self.show()

    def click(self):
        self.say += 1
        self.yaziAlani.setText("Bana " + str(self.say) + " kere tıklandı")


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()
sys.exit(app.exec_())
