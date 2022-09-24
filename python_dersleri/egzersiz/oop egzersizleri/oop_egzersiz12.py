class Computation():
    def __init__(self):
        pass

    def Factorial(self, sayi):
        faktoriyel = 1
        if(sayi == 0 or sayi == 1):
            print(faktoriyel)

        else:
            for i in range(1, sayi + 1):
                faktoriyel *= i
            print(faktoriyel)

    def Sum(self, sayi):
        toplam = 0
        for i in range(1, sayi + 1):
            toplam += i
        print(toplam)
    
    def testPrims(self, sayi):
        count = 0
        for i in range(1, sayi):
            if(sayi % i == 0):
                count += 1
            else:
                continue
        if(count == 1):
            print("{} asaldır.".format(sayi))
        else: 
            print("{} asal değildir.".format(sayi))

    def isPrim(self, sayi):
        count = 0
        for i in range(1, sayi):
            if(sayi % i == 0):
                count += 1
            else:
                continue
        if(count == 1):
            return True
        else: 
            return False
        

    def tableMult(self, sayi):
        for i in range(1, 11):
            print(i*sayi)

    def allTablesMult(self):
        j = 1
        for i in range(1,11):
            print("*************************")
            for j in range(1,11):
                print("{} x {} = {}".format(i,j,i*j))

    def listDiv(self, sayi):
        liste = list()
        for i in range (1, sayi+1):
            if(sayi % i == 0):
                liste.append(i)
            else:
                continue
        print("{} sayısının bölenleri: {}".format(sayi, liste))

    def listDivPrim(self, sayi):
        liste = list()
        for i in range (1, sayi+1):
            if((sayi % i == 0) and self.isPrim(i)):
                liste.append(i)
            else:
                continue
        print(liste)
        



s = Computation()
"""s.Factorial(2)
s.Sum(5)
s.testPrims(3)
s.tableMult(5)
s.allTablesMult()"""
s.listDiv(250)
s.listDivPrim(84)
