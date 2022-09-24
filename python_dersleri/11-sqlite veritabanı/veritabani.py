import sqlite3

con = sqlite3.connect("C:/Users/Emre Güler/Documents/SEVRO49/YAZILIM/PYTHON/vscode/python dersleri/sqlite veritabanı/kütüphane.db") # con = connection. kütüphane adında veritabanı varsa bağlanır, yoksa oluşturup bağlanır.

cursor = con.cursor() # veritabanında gezmek için imleç gerekiyor.

def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT) ")
    con.commit() # kodları işler. yazmazsak çalışmaz.

def veriEkle():
    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit() # her girişimizde veritabanı güncellenir.

def veriEkle2(isim, yazar, yayınevi, sayfaSayisi): # kullanıcıdan veri alan metot
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfaSayisi)) # soru işareti yerine geçer.
    con.commit()

def veriAl():
    cursor.execute("SELECT * From kitaplık") # kitaplık veritabanındaki tüm verileri getirir.
    liste = cursor.fetchall() # işlem yaptığımız cursor üzerindeki tüm verileri getirir.
    print("Kitaplık tablosunun bilgileri")
    for i in liste:
        print(i)

def veriAl2():
    cursor.execute("SELECT İsim, Yazar From kitaplık") # sadece belli verileri çekmemizi sağlar.
    liste = cursor.fetchall()
    print("\n*********Verial2 tablosu*********")
    for i in liste:
        print(i)

def veriAl3(yayinevi):
    cursor.execute("SELECT * From kitaplık where Yayınevi = ?",(yayinevi,)) # belli bir yayınevindeki kitapları döndürür.
    liste = cursor.fetchall()
    print("\n*********Verial3 tablosu*********")
    for i in liste:
        print(i)

def verileriGuncelle(eskiYayinevi, yeniYayinevi):
    cursor.execute("UPDATE kitaplık SET Yayınevi = ? where Yayınevi = ?",(yeniYayinevi, eskiYayinevi))
    con.commit()

def verileriSil(yazar):
    cursor.execute("DELETE From kitaplık where Yazar = ?",(yazar,))
    con.commit()



    

"""isim = input("İsim: ")
yazar = input("Yazar: ")"""
#yayinevi = input("Yayınevi: ")
#sayfaSayisi = int(input("Sayfa Sayısı: "))
tabloOlustur()
#veriEkle()
#veriEkle2(isim, yazar, yayınevi, sayfaSayisi)
veriAl()
#veriAl2()
#veriAl3(yayinevi)

"""eskiYayinevi = input("Eski yayınevi: ")
yeniYayinevi = input("Yeni yayınevi: ")
verileriGuncelle(eskiYayinevi, yeniYayinevi)"""
veriAl()
yazar = input("Yazar: ")
verileriSil(yazar)
veriAl()


con.close() # bağlantıyı kesmemiz gerekiyor.