"""print("Em" in "Emre") # True veya False döndürür
print( not 5 in [1,2,3,4])

liste = [1,2,3,4,5,6,7]

for eleman in liste: # foreach
    print(eleman)

toplam = 0
for eleman in liste:
    toplam += eleman
print(toplam) """

"""liste = [1, 2, 3, 4, 34, 54, 63, 78]

for eleman in liste:
    if eleman % 2 == 0:
        print(eleman, sep = ",")

liste2 = [(1,2),(3,4),(5,6)]

for (i,j) in liste2:
    print(i,j)

for eleman in liste2:
    print(eleman) """

sozluk = {"bir":1, "iki":2}

for eleman in sozluk.items():
    print(eleman)