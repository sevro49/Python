"""
Kullanıcıdan iki sayı isteyin ve bunların değerini birbiriyle değiştirin
"""

a = int(input("Lütfen 1. sayıyı girin: "))
b = int(input("Lütfen 2. sayıyı girin: "))

a,b = b,a

print("1: {}, 2: {}".format(a,b))