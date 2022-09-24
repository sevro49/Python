liste = ["Elma", "Armut", "Muz", "Kiraz"]

# sonucu [0, 'Elma'),(1, 'Armut'), (2,'Muz'), (3,'Kiraz')] yapalım

sonuc = list()

i = 0

for a in liste:

    sonuc.append((i,a))
    i += 1

print(sonuc)

"""Enumerate fonksiyonu her bir elemanı indekslerle numaralandırıyor."""

print(list(enumerate(liste)))

for i,j in enumerate(liste):
    print(i,j)

liste = ["a", "b", "c", "d"]
for i,j in enumerate(liste):
    if(i % 2 == 0):
        print(j)