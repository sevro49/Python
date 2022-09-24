"""
kullanıcıdan alınan boy ve kilo değerlerine göre been kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın
"""

boy = int(input("Boyunuzu giriniz (cm): "))
kilo = int(input("Kilonuzu giriniz (kg): "))

bkt = kilo / (boy * 0.01 * boy * 0.01)

print("Beden Kitle İndeksiniz:", bkt)
if bkt < 18.5:
    print("Zayıf")
elif (bkt >= 18.5 and bkt < 25):
    print("Normal")
elif (bkt >= 25 and bkt < 30):
    print("Fazla kilolu")
elif bkt > 30:
    print("Obez")
else:
    print("Geçersiz bir değer girdiniz!!")
