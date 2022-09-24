import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont
from random import randint

class Dice(QWidget):

    def __init__(self):

        super().__init__()

        self.setGeometry(150,150,500,500)
        self.setWindowTitle("Rolling a Dice")
        self.show()
        self.Ui()


    def Ui(self):
        self.rollDice = QPushButton("ROLL DICE")
        self.rollDice.setFont(QFont("Times New Roman", 15))

        self.label = QLabel("")
        self.label.setFont(QFont("Times new Roman", 300))

        vBox = QVBoxLayout()
        vBox.addWidget(self.rollDice)
        vBox.addWidget(self.label)

        hBox = QHBoxLayout()
        hBox.addStretch()
        hBox.addLayout(vBox)
        hBox.addStretch()

        self.rollDice.clicked.connect(self.RollDice)
        self.setLayout(hBox)
        
    def RollDice(self):
        result = randint(0, 6)
        self.label.setText(str(result))

app = QApplication(sys.argv)
dice = Dice()
sys.exit(app.exec_())