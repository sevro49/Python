from datetime import date, datetime
import locale

locale.setlocale(locale.LC_ALL,"")
suAn = datetime.now()
print(suAn.now())
print(suAn.year)
print(suAn.month)
print(suAn.day)
print(suAn.hour)
print(datetime.ctime(suAn))  # tarihi daha güzel gösterir

print(datetime.strftime(suAn, "%Y"))  # yıl ismini verir
print(datetime.strftime(suAn, "%B"))  # ay ismini verir
print(datetime.strftime(suAn, "%A"))  # gün ismini verir
print(datetime.strftime(suAn, "%X"))  # saat bilgisini verir
print(datetime.strftime(suAn, "%D"))  # gün billgisini verir

suAn2 = datetime.now()
saniye = datetime.timestamp(suAn2) # şu anki zamanı saniye cinsinden bulur
print(saniye)

suAn3 = datetime.fromtimestamp(saniye) # saniye cinsinden verilmiiş bir zamanı datetime objesine çevirir.
print(suAn3)

print(datetime.fromtimestamp(0)) #epoch zamanı
tarih = datetime(2023,7,20)
fark = tarih - suAn
print("iki tarih arasındaki fark",fark)