from multiprocessing.sharedctypes import Value


def cift_mi(sayi):
    
    if (sayi % 2 == 0):
        return sayi

    else:
        raise ValueError

liste = [34, 2, 1, 33, 100, 61, 10000]

for i in liste:
    try:
        print(cift_mi(i))
    except ValueError:
        pass