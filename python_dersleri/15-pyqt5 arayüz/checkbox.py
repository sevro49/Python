import sys
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QLabel, QPushButton, QVBoxLayout


class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.checkbox = QCheckBox("Python'u seviyor musunuz?")
        self.yaziAlani = QLabel("")
        self.buton = QPushButton("Bana tıkla")

        vBox = QVBoxLayout()
        vBox.addWidget(self.checkbox)
        vBox.addWidget(self.yaziAlani)
        vBox.addWidget(self.buton)

        self.setLayout(vBox)
        self.setWindowTitle("Check box")
        

        # lambda = fonksiyon çağrısı yerine fonkisyon objesi olarak kullanırız.
        self.buton.clicked.connect(lambda: self.click(self.checkbox.isChecked(), self.yaziAlani))
        self.show()

    def click(self, checkbox, yaziAlani):
        if checkbox:
            yaziAlani.setText("Pythonu seviyorsun. çok güzel")
        else:
            yaziAlani.setText("Neden sevmiyorsun??")


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
