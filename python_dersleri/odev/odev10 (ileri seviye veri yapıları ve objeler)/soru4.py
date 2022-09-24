"""Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , 
ekrana isim ve soyisimleri isimlere göre sıralı bir şekilde yazdırmaya çalışın.

        isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]"""


isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

i = 0
while(i < len(isim)):
    isim[i] += " " + soyisim[i]
    i+= 1
    
isim.sort()
print(isim)
