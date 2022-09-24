"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı 
bilgilerini alın ve sürücünün toplam ne kadar ödemesi gerektiğini hesaplayın
"""

fiyat = float(input("km başı kaç tl yakıyor? "))
yol = int(input("Kaç km yol yaptınız? "))

toplam = yol * fiyat

print("Toplam ödemeniz gereken ücret:",toplam)