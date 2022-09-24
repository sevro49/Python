from forex_python.converter import CurrencyRates
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QComboBox


class Currency(QWidget):

    def __init__(self):
        super().__init__()

        self.window()

    def window(self):

        self.combo = QComboBox()
        self.combo.addItem("USD")
        self.combo.addItem("TRY")
        self.combo.addItem("EUR")
        self.combo.addItem("GBP")

        self.combo2 = QComboBox()
        self.combo2.addItem("TRY")
        self.combo2.addItem("USD")
        self.combo2.addItem("EUR")
        self.combo2.addItem("GBP")

        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Enter Amount")
        self.lineEdit2 = QLineEdit()

        
        vBox = QVBoxLayout()
        vBox.addStretch()
        vBox.addWidget(self.combo)
        vBox.addWidget(self.lineEdit)
        vBox.addStretch()

        vBox2 = QVBoxLayout()
        vBox2.addStretch()
        vBox2.addWidget(self.combo2)
        vBox2.addWidget(self.lineEdit2)
        vBox2.addStretch()

        self.exchangeBtn = QPushButton("Exchange")
        self.exchangeBtn.setShortcut("Return")

        hBox = QHBoxLayout()
        hBox.addLayout(vBox)
        hBox.addStretch()
        hBox.addWidget(self.exchangeBtn)
        hBox.addStretch()
        hBox.addLayout(vBox2)

        self.setLayout(hBox)
        self.setWindowTitle("Currency Exchange")
        self.setGeometry(1200, 100, 350, 150)
        self.exchangeBtn.clicked.connect(self.exchange)
        self.show()

    def exchange(self):
        c = CurrencyRates()
        amount = float(self.lineEdit.text())
        currency = amount * (c.get_rate(self.combo.currentText(), self.combo2.currentText()))
        self.lineEdit2.setText(str(currency))

app = QApplication(sys.argv)
exchance = Currency()
sys.exit(app.exec_())
