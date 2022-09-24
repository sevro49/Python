liste1 = [1,2,3,"Emre",4,5]
print("1-",liste1)

liste2 = list()
print("2-",liste2) # boş liste.

print("3- boyut:",len(liste1)) # liste boyutunu verir.

liste2 = [1,2,3,4,5,6,7,8,9,10]
print("4-",liste2[4]) # 4. indisteki elemanı verir.
print("5-",liste2[-1]) # son elemanı verir.
print("6-",liste2[-3]) # sondan 3. elemanı verir.
print("7-",liste2[4:7]) # 4. ve 7. indislerdeki elemanlar arasındaki elemanları verir (7. eleman dahil değil)
print("8-",liste2[::2]) # ilk eleman dahil ikişer ikişer atlayarak listeyi yazdırır.
print("9-",liste2[::-1]) # listeyi tersten yazdırır.

liste3 = list("MERHABA") # listeyi index index yazdırır.
print("10-",liste3)   

liste4 = [1,2,3]
liste5 = [4,5,6]
liste6 = liste4 + liste5
print("11-",liste6)

liste4[:2] = 7,8 # listenin ilk 2 elemanını 7 ve 8 ile değiştirdik.
print("12-",liste4)

liste4.append(50) # liste sonuna eleman ekler.
print("13-",liste4)

liste4.pop() # index numarası belirtilirse o indexteki elemanı, belirtilmezse son elemanı listeden çıkartır.
print("14-",liste4)

liste7 = [1,2,10,5,50,24,22,13,17]
liste7.sort() # listeyi küçükten büyüğe sıralar.
print("15-",liste7)
liste7.sort(reverse = True) # listeyi büyükten küçüğe sıralar.
print("16-",liste7)

liste8 = ["Emre", "Elif", "Ahmet", "Hatice", "Mustafa"]
liste8.sort() # listeyi alfabetik olarak sıralar. Ters sıralama burada da geçerli
print("17-",liste8)

liste9 = [[1,2],[49,50]] # liste içinde liste 
print("18-",liste9[1][0]) # [1][0] --> 1 = [49,50] | 0 = 49 