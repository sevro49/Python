def toplama(a,b,c):
    print("Toplam =",a+b+c)

def ikiyleCarp(a):
    print("ikiyle çarpılmış hali = ", a*2)

def toplama(a,b,c):
    return a+b+c

def ikiyleCarp(a):
    return a*2

toplam = toplama(10,20,30)
#print(ikiyleCarp(toplam))

def ucleCarp(a):
    print("1. Fonksiyon çalıştı")
    return a*3

def ikiyleTopla(a):
    print("2. Fonksiyon çalıştı")
    return a + 2

def dordeBol(a):
    print("3. Fonksiyon çalıştı.")
    return a / 4

print(ucleCarp(ikiyleTopla(dordeBol(12))))
