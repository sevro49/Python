"""
kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın
"""

a = int(input("1. sayı: "))
b = int(input("2. sayı: "))
c = int(input("3. sayı: "))

if ((a > b and a > c) or (a >= b and a >= c)):
    print(a)
elif ((b > a and b > c) or (b >= a and b >= c)) :
    print(b)
elif ((c > a and c > b) or (c >= a and c >= b)):
    print(c)
