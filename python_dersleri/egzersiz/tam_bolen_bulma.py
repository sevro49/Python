def tamBolenleriBulma(sayi):
    tam_bolenler = []

    for i in range(1,sayi):
        if (sayi % i == 0):
            tam_bolenler.append(i)

    return tam_bolenler

while True:

    sayi = input("Sayi (çıkmak için 'q': ")

    if (sayi == 'q'):
        break
    else:
        sayi = int(sayi)
        print("Tam bölenler: ", tamBolenleriBulma(sayi))