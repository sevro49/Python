# append metodunu hatırlayalım
liste1 = [1, 2, 3, 4, 5]

liste2 = []

for i in liste1:  # append yöntemi ile ekleme.
    liste2.append(i)
print(liste2)

liste3 = [1, 2, 3, 4, 5]

liste4 = [i for i in liste3]  # list comprehension ile ekleme.
print(liste4)

liste5 = [3, 4, 5]

liste6 = [i*2 for i in liste5]
print(liste6)


liste7 = [(1, 2), (3, 4), (5, 6)]
liste8 = [i*j for i, j in liste7]
print(liste8)

str = "Python"
liste9 = [i*3 for i in str]
print(liste9)

liste10 = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]]
liste11 = []
#yeni_liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in liste10:               #for döngüsü ile
    for x in i:
        liste11.append(x) 
print(liste11)

liste11 = []
liste11 = [x for i in liste10 for x in i]
print(liste11)
