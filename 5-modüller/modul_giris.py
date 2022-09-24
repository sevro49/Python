"""#import math

# print(dir(math)) #hangi modül içinde ne olduğunu gösterir.
# print(help(math)) # hangi fonksiyonun ne işe yaradığını gösterir.

#print(math.factorial(5))
#print(math.floor(5.6))
#print(math.ceil(5.6))

#import math as matematik #math kullanmak yerine matematik olarak

#print(matematik.ceil(5.6))
#print(matematik.factorial(5))

from math import floor, ceil # 2 tane fonksiyon import etmiş olduk
print(floor(5))

from math import * # math modülü içindeki tüm fonksiyonları dahil eder.

print(factorial(5)) # tüm fonksiyonları dahil ettiğimiz için bu şekilde kullanabiliriz."""

def factorial (sayi):
    print("Benim fonksiyonum")

    faktoriyel = 1
    if (sayi == 0 or sayi == 1):
        return 1
    else:
        while(sayi >= 1):
            faktoriyel *= sayi
            sayi -= 1
        return faktoriyel

from math import *

print(factorial(5)) # son gördüğü fonksiyonu aldığı  için math modülünü kullanır