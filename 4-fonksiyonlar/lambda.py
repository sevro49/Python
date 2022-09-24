liste1 = [1, 2, 3, 4, 5]
liste2 = [i*2 for i in liste1]
print(liste2)

# lambda ifadesi tek satır halinde fonksiyon oluşturmaya yarar.


def ikiyleCarp(x):      # klasik fonksiyon tnaımlama
    return x * 2


print(ikiyleCarp(3))


def ikiyleCarp2(x): return x * 2  # lambda ile fonksiyon tanımlama


print(ikiyleCarp2(6))


def toplama(x, y, z):
    return x + y + z


print(toplama(1, 2, 3))


def toplama2(x, y, z): return x + y + z


print(toplama2(10, 20, 30))


def tersCevir(s):
    return s[::-1]


print(tersCevir("Emre"))


def tersCevir2(s): return s[::-1]


print(tersCevir2("Ahmet"))


def cifttek(sayi):
    return sayi % 2 == 0


print(cifttek(14))
print(cifttek(15))


def cifttek2(sayi): return sayi % 2 == 0


print(cifttek2(10))
print(cifttek2(11))
