# kümeler matematikte olduğu gibi bir elemandan bir adet tutan veri tipidir.

x = set() # boş küme
print(type(x)) # set

liste=[1,2,3,3,1,1,2,2,2] # aynı elemanı birçok defa barındıran bir liste

x = set(liste) # aynı elemanlar tek bir elemana indirgendi

print(x) 

x = set("Python Programlama Dili")  # aynı karakterler tek bir karaktere indirgendi
print(x) 

x = {"Emre","Zeynep","Emre"}
print(x)

x = {"Elma","Armut","Kiraz","Muz"}

for i in x:
    print(i) # kümeler sırasızdır.

x = {"Python","Php","Java","Javascript"}
# print(x[0]) # hata verir. for döngüsü ile bastırabiliriz ya da listeye çeviririz

liste = list(x)
print(liste[1])


#add(): Kümeye ekleme işlemi yapar. Aynı elemanı eklemeye çalışırsak hata vermez ama herhangi bir ekleme de yapmaz.
x = {1,2,3}
x.add(4)
print(x)
x.add(4) # tekrar ekleme yapmıyor. 
print(x)


#difference(): birinci kümenin ikinci kümeden farkını döner
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}

print(kume1.difference(kume2))
print(kume2.difference(kume1))

print(kume1)
print(kume2) ## iki küme de aynı kalmıştır. fark alma yoktur.


#difference_update(): birinci kümenin ikinci kümeden farkını dönerek birinci kümeyi bu farka göre günceller.
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
kume1.difference_update(kume2)
print(kume1)


#discard(): içine verilen değer kümeden çıkartılır. öyle bir değer yoksa hata vermezi ama hiçbir şey de yapmaz.
kume1.discard(3)
print(kume1)


#intersection(): küme kesişimlerini bulmamızı sağlar
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
print(kume1.intersection(kume2))


#intersection_update(): küme kesişimlerini bulur ve birinci kümeyi bu kesişime göre günceller
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
kume1.intersection_update(kume2)
print(kume1)


#isdisjoint(): kümelerin kesişimi boş ise True değilse False döner
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
kume3 = {30,40,50}

print(kume1.isdisjoint(kume2))
print(kume1.isdisjoint(kume3))


# issubset(): birinci kume ikinci kümenin alt kümesiyse True, değilse False döner
kume1 = {1,2,3}
kume2 = {1,2,3,4}
kume3 = {5,6,7}

print(kume1.issubset(kume2))
print(kume1.issubset(kume3))


#union(): iki kümenin birleşim kümesini döner
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}

print(kume1)
kume1.union(kume2)
print(kume1)
print(kume1.union(kume2))