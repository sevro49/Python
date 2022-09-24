"""
Kulanıcının girdiği vize1, vize2, final notlarına göre harf notunu hesaplayın

vize1, toplam notun %30'una etki edecek.
vize2, toplam notun %30'una etki edecek.
final, toplam notun %40'ına etki edecek.
"""

vize1 = int(input("Vize 1: "))
vize2 = int(input("Vize 2: "))
final = int(input("Final: "))
toplam = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)

if toplam >= 90:
    print("AA")
elif toplam >= 85:
    print("BA")
elif toplam >= 80:
    print("BB")
elif toplam >= 75:
    print("CB")
elif toplam >= 70:
    print("CC")
elif toplam >= 65:
    print("DC")
elif toplam >= 60:
    print("DD")
elif toplam >= 55:
    print("FD")
else:
    print("FF")
