print("""*****************
Kullanıcı girişi programı
*****************
""")

sys_kullanici_adi = "Emre"
sys_parola = "12345"
giris_hakki = 3

while True:
    kullanici_adi = input("Kullanıcı Adı: ")
    parola = input("Parola: ")
    if(kullanici_adi != sys_kullanici_adi and parola == sys_parola):
        print("Kullanıcı adı hatalı!!")
        giris_hakki -= 1
        print("Kalan giriş hakkı",giris_hakki)
    elif(kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Parola hatalı!!")
        giris_hakki -= 1
        print("Kalan giriş hakkı",giris_hakki)
    elif(kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanıcı adı ve parola hatalı!!")
        giris_hakki -= 1
    else:
        print("Giriş başarılı")
        break
    if (giris_hakki == 0):
        print("Girş hakkınız bitti...")
        break