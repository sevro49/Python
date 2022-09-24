"""1'den 10'a kadar olan sayılarla ekrana çarpım tablosu yazdırın."""

liste1 = [*range(1,11)]
j = 1

for i in liste1:
    print("**************************")
    for j in liste1:
        print("{} x {} = {}".format(i,j,i*j))

    

    