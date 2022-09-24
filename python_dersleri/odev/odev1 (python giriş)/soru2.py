"""Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun

Beden kitle indeksi = Kilo / Boy(m) * Boy(m)

"""

kilo = int(input("Kilonuzu girin: "))
boy = int(input("Boyunuzu girin (cm):"))

bkt = kilo / ((boy * 0.01) * (boy * 0.01))

print("Beden kitle indeksiniz:",bkt)
