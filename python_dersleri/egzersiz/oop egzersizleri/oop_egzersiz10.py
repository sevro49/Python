import time

class BankAccount():
    def __init__(self, accountNumber, name, balance = 0):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self):
        deposit = int(input("Yatırmak istediğiniz mikarı giriniz: "))
        print("Para yatırılıyor...")
        time.sleep(1)
        self.balance += deposit
        print("Yatırılan:",deposit)
        print("Güncel bakiyeniz:",self.balance)

    def Widthdraw(self):
        print("Toplam bakiyeniz:",self.balance)
        widthdraw = int(input("Çekmek istediğiniz miktarı giriniz: "))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        if(widthdraw > self.balance):
            print("Yetersiz bakiye!!")
        else:
            self.balance -= widthdraw
            print("Çekilen:",widthdraw)
            print("Güncel bakiyeniz:",self.balance)

    def bankFees(self):
        bankFee = self.balance * 0.05
        self.balance -= bankFee
        print("İşlem ücreti:",bankFee)
        print("Güncel bakiyeniz:",self.balance)

    def display(self):
        print("The account number of this account is:",self.accountNumber)
        print("Name of owner of this account is:",self.name)
        print("The balance is:",self.balance)

emre = BankAccount(123456789, "Emre Güler", 100000)
emre.Deposit()
emre.Widthdraw()
emre.bankFees()
emre.display()
        



    

