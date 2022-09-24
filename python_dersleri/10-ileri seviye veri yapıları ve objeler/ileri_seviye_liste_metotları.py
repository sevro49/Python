#append(): liste sonuna eleman ekler

liste = [1,2,3,4,5,6,7]
liste.append(49)
liste.append("Emre")
print(liste)


#extend(): bir listeye başka listeden bir eleman eklemeyi sağlar
liste1 = [1,2,3,4,5,6,7]
liste2 = [10,20,30]
liste1.extend(liste2)
print(liste1)


#insert(): belli bir indekse eleman eklemeyi sağlar

liste=[1,2,3,4,5,6,7,8,9]
liste.insert(2,"Python")
print(liste)


#pop(): içine değer vermezsek listenin son elemanını siler. değer verirsek o indexteki elemanı siler

liste = [1,2,3,4,5,6,7]

liste.pop()
print(liste)
liste.pop(3)
print(liste)


#remove(): verdiğimiz değeri listeden çıkartır.

liste = ["Python","Php","Java","C"]
liste.remove("Php")
print(liste)


#index(): verilen bir değeri baştan başlayarak arar, hangi indexte olduğunu söyler. değer listede yoksa hata verir. ekstra değer verilirse o indexten aramaya başlar

liste = [1,2,3,4,5,3,3,6,7,8,9]
print(liste.index(3))
print(liste.index(3,3))


#count(): verilen değerin listede kaç defa geçtiğini sayar

liste = [1,2,3,4,5,3,3,6,7,8,3,3,9]
print(liste.count(3))


#sort(): bir listedeki elemanları küçükten büyüğe ya da alfabetik olarak sıralar. içine (reverse = True) değeri verilirse tersten sıralar

liste = [12,-2,3,1,34,100]
liste.sort()
print(liste)
liste.sort(reverse=True)
print(liste)
liste = ["Python","Php","Java","C"]
liste.sort()
print(liste)