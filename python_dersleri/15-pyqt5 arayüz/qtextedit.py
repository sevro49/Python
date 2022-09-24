import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QTextEdit, QPushButton, QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yaziAlani = QTextEdit()
        self.yaziAlani.setPlaceholderText("Bu bir yazı alanıdır...")
        self.temizle = QPushButton("Temizle")
        vBox = QVBoxLayout()
        vBox.addWidget(self.yaziAlani)
        vBox.addWidget(self.temizle)

        self.setLayout(vBox)
        self.setWindowTitle("yazı alanı")
        self.temizle.clicked.connect(lambda: self.click())
        self.show()

    def click(self):
        self.yaziAlani.clear()


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())