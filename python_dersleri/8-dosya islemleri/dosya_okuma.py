#'r' kipi (read). Dosya okumaya yarar.

"""file = open("C:/Users/Emre Güler/Desktop/Emre.txt","r")

#1
for i in file: # her bir satırı tek tek yazdırır.
    print(i, end = "") # dosyaya yazarken \n koyuyoruz. for döngüsü de koyuyor. for döngüsündekini iptal etmek için (end = "") kullanabiliriz.

file.close()

#2
file = open("C:/Users/Emre Güler/Desktop/Emre.txt","r")
icerik = file.read()
print(icerik)
file.close()

#3
file = open("C:/Users/Emre Güler/Desktop/Emre.txt","r")
print(file.readline()) #satır satır okuma yapar. okuyacak bir şey kalmazsa boş string döndürür.
print(file.readline())

file.close()

#4 
file = open("C:/Users/Emre Güler/Desktop/Emre.txt","r")
liste = file.readlines() # dsoyaları liste olarak okur.
print(liste)
file.close()"""


"""
dosyaları otomatik kapatma

with open(dosya_adi, dosya_kipi) as file:
    dosya işlemleri
    
"""

with open("C:/Users/Emre Güler/Desktop/Emre.txt","r") as file:
    for i in file:
        print(i,end="")
