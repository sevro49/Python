print("""******************************
Kullanıcı Girişi
******************************
""")

sys_kullanici_adi = "Emre"
sys_parola = "12345"

kullanici_adi = input("Kullanıcı Adı: ")
parola = input("Parola: ")

if (kullanici_adi == sys_kullanici_adi and sys_parola != parola):
    print("Hatalı şifre girdiniz.")
elif (kullanici_adi != sys_kullanici_adi and sys_parola == parola):
    print("Kullanıcı adı hatali!!")
elif(kullanici_adi != sys_kullanici_adi and sys_parola != parola):
    print("Kullanıcı adı ve şifre hatalı!!")
else:
    print("Sisteme başarıyla giriş yaptınız!")