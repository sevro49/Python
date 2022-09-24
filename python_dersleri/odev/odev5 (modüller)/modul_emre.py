def faktoriyel(a):
    """
    Bu fonksiyon, faktöriyel hesaplar
    """
    faktoriyel = 1
    i = 1
    a = int(a)
    while i <= a:
        if(a == 1 or a == 0):
            faktoriyel = 1
            break
        else:
            faktoriyel *= i
            i += 1

    print(faktoriyel)


def ceil(a):
    """
    Bu fonksiyon, girdiğiniz değeri bir üstteki sayıya yuvarlar
    """
    if(a % 1 != 0):
        a = (a // 1) + 1

    print(float(a))


def floor(a):
    """
    Bu fonksiyon, girdiğiniz değeri bir alttaki sayıya yuvarlar
    """
    if(a % 1 != 0 or a % 1 == 0):
        a = (a // 1)

    print(float(a))


