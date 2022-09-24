"""
dosyaları ileri sarmak için seek() fonksiyonunu kullanıyoruz. Ama ondan önce dosya imlecinin nerede olduğunu görmek için tell() 
metodunu kullanmamız gerekiyor.
"""

with open("C:/Users/Emre Güler/Desktop/Emre.txt","r") as file:
    print(file.tell())
    file.seek(10) # imleci 10. byte'a gönderdik
    print(file.tell())

with open("C:/Users/Emre Güler/Desktop/Emre.txt","r") as file:
    file.seek(2)
    icerik = file.read(6) # 6 byte okur
    print(file.tell())
    print(icerik)