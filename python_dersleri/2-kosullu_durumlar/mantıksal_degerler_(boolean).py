# True veya False değerini alabilir.
a = True
print("1-", type(a))  # tipini verir
b = False
print("2-", type(b))  # tipini verir

print("3-", bool(49))  # True
print("4-", bool(-234))  # True
print("5-", bool(123.123))  # True
print("6-", bool(0))  # False
print("7-", bool(0.0))  # False
print("8-", bool(8 > 9))  # False

a = None  # hemen değer atamak istemiyorsak bu şekilde kullanabiliriz.
print("9-", a)
a = 49  # şimdi değer atıyoruz.
print("10-", a)

print("11-", bool("Emre" == "Emre"))  # True
print("12-", bool("Emre" == "Ahmet"))  # False
