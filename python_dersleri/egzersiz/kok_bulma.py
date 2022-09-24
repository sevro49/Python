"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem: ax^2 + bx + c

Deltayı Hesaplama: b ** 2 - 4 * a * c

Birinci kök: (-b - delta ** 0.5) / (2*a)
İkinci kök: (-b + delta ** 0.5) / (2*a)

"""

print("ikinci dereceden kök bulma programı\n")
print("denklem şu şekildedir: 'ax^2 + bx + c'. sizden istenen a, b ve c yerine değerler vermeniz. Bu sayede program kökleri hesaplayacaktır.")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 - 4*a*c

kok1 = (-b - delta ** 0.5) / (2*a)
kok2 = (-b + delta ** 0.5) / (2*a)

print("Kök 1: {}\nKök 2: {}\n".format(kok1,kok2))