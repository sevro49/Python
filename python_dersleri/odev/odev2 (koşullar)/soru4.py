"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;

abs(-4)
4
abs(5)
5
"""

cevap = input("\n\nÜçgen tipini mi bulmak istersiniz dörtgen dipini mi? ")

if (cevap.lower() == "ucgen"):
    print("\nÜçgenin kenarlarını giriniz")
    a = int(input("Kenar 1: "))
    b = int(input("Kenar 2: "))
    c = int(input("Kenar 3: "))

    if (not(abs(a-b) < c < a+b)):
        print("Üçgen belirtmiyor")
    elif (not(abs(a-c) < b < a+c)):
        print("Üçgen belirtmiyor")
    elif (not(abs(b-c) < a < b+c)):
        print("Üçgen belirtmiyor")

elif (cevap.lower() == "dortgen"):
    print("\nDörtgenin kenarlarını giriniz")
    a = int(input("Kenar 1: "))
    b = int(input("Kenar 2: "))
    c = int(input("Kenar 3: "))
    d = int(input("Kenar 4: "))

    if (a == b == c == d):
        print("KARE")
    elif (a == c and b == d):
        print("DİKDÖRTGEN")
    else:
        print("SIRADAN DÖRTGEN")

    
