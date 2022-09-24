import sys
from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QLabel, QPushButton, QVBoxLayout


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radioYazisi = QLabel("Hangi dili daha çok seviyorsun?")
        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")
        self.php = QRadioButton("Php")

        self.yaziAlani = QLabel("")
        self.buton = QPushButton("Gönder")

        vBox = QVBoxLayout()
        vBox.addWidget(self.radioYazisi)
        vBox.addWidget(self.java)
        vBox.addWidget(self.python)
        vBox.addWidget(self.php)
        vBox.addStretch()
        vBox.addWidget(self.yaziAlani)
        vBox.addWidget(self.buton)

        self.setLayout(vBox)
        self.buton.clicked.connect(lambda: self.click(self.python.isChecked(
        ), self.java.isChecked(), self.php.isChecked(), self.yaziAlani))

        self.setWindowTitle("RadioButton")
        self.show()

    def click(self, python, java,  php, yaziAlani):
        if python:
            yaziAlani.setText("Python")

        if java:
            yaziAlani.setText("Java")
        if php:
            yaziAlani.setText("Php")


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
