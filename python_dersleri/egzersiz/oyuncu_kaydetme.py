print("Oyuncu Kaydetme Programı")

ad = input("Oyuncu adını girin: ")
soyad = input("Oyuncu soyadını girin: ")
takim = input("Oyuncu takımını girin: ")

bilgiler = [ad,soyad,takim]
print("Bilgiler kaydediliyor...")
print("\nOyuncu adı: {}\nOyuncu soyadı: {}\nOyuncu takımı: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))
print("Bilgiler kaydedildi...")