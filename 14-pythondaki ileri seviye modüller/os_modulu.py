"""
os modülü işletim sisteminde işlemler gerçekleştirebilidiğimiz standard bir python modülüdür."""

import os
from datetime import datetime

#print(dir(os))

#print(os.getcwd()) # bu modülün bulunduğu yeri gösterir.
#print(os.listdir()) # bu directorydeki dosyaları listeler

# os.mkdir("Deneme22") #bulunan directoryde dosya oluşturur
# os.makedirs("Deneme2/Deneme3") # dosya içinde dosya oluşturmaya yarar
# os.rmdir("Deneme2/Deneme3") # dosya siler
# os.removedirs("Deneme2/Deneme3") # alt dosyalar da dahil tüm dosyaları siler.
# os.rename("test.txt","test2.txt") #dosyayı yeniden adlandırır.
# print(os.stat("test2.txt"))
# print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime)) # dosya ile ilgili bilgileri verir

#print(os.walk("C:Users/Emre Güler/Desktop"))

for i in os.walk("C:/Users/emreg/Desktop"):
    print(i)
# print(os.listdir())
