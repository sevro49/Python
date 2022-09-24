"""
Generatorlar pythonda iterable objeler oluşturmak için kullanılan objelerdir ve bellekte herhangi bir yer kaplamazlar.
Örneğin, 100.000 tane değer üretim bu değerleri bellekte tutmak oldukça fazla yer kaplayacaktır. O yüzden bu işlemi gerçekleştiren
fonkisoynu generator fonksiyon şeklinde yazmak oldukça mantıklı olacaktır."""

#generator kullanmadan yazılan bir fonksiyon:

def kareAl():
    sonuc = list()

    for i in range(1,6):
        sonuc.append(i ** 2)

    return sonuc

print(kareAl())


#generator kullanrak yazılan bir fonksiyon

def kareAl2():
    for i in range(1,6):
        yield i ** 2 # generator kullanımı. bellekte saklanmaz.

generator = kareAl2()
print(generator)

iterator = iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

iterator2 = iter(generator)
# print(next(iterator2)) # generator bellekte tutmadığı için hata verir

liste = [i * 3 for i in range(5)]
print(liste)
generator = (i * 3 for i in range(5))
iterator = iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


def carpimTablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)

for i in carpimTablosu():
    print(i)
