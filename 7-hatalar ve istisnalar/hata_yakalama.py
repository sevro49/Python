try:
    a = int("dfgdfg")
    print("Program burada")
except:
    print("Bir hata oluştu")
print("Hata1")

try:
    a = int(23)
    print("Program burada")
except:
    print("Bir hata oluştu")
print("Hata1")

try:
    a = int("dfgdfg")
    print("Program burada")
except ValueError:
    print("Bir hata oluştu")
print("Hata2")

"""try:
    a = int(input("Sayı 1: "))
    b = int(input("Sayı 2: "))
    print(a / b)
except ValueError:
    print("İnputu doğru girin")
except ZeroDivisionError:
    print("bir sayı 0'a bölünemez")"""
"""
try:
    a = int(input("Sayı 1: "))
    b = int(input("Sayı 2: "))
    print(a / b)
except ValueError:
    print("İnputu doğru girin")
except ZeroDivisionError:
    print("bir sayı 0'a bölünemez")
finally: #hata olsa da olmasa da mutlaka çalışacak kodlar buraya yazılır.
    print("Bunu kesin bastır")"""

"""
raise HataAdı (opsiyonel hata mesajı)"""

def terscevir(s):
    if (type(s) != str):
        raise ValueError("lütfen string bir değer gönderin.")
    else: 
        return s[::-1]

print(terscevir("Python"))
# print(terscevir(12))

try:
    print(terscevir(12))
except ValueError:
    print("Fonksiyon hata verdi")






