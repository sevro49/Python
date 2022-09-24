def fonksiyon():
    a = 10  # yerel değişken.
    print(a)


fonksiyon()


b = 5  # global değişken.


def fonksiyon2():
    print(b)


fonksiyon2()
print(b)


c = 10


def fonksiyon3():
    c = 2
    print(c)


fonksiyon3()  # yerel değişken kullanılır.
print(c)  # global değişken kullanılır.


d = 5


def fonksiyon4():
    global d  # global d değerini kullanmak istediğimizi belli ediyoruz.
    d = 3
    print(d)


fonksiyon4()  # 3
print(d)  # 3


if True:
    e = 4
    print(e)
print(e)    # if veya while bloğu içinde tanımlanan değişkenler globaldir.
