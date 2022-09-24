"""1'den 1000'e kadar olan sayılardan asal sayıları üreten generator bir fonksiyon yazın."""

def asal():
    for i in range(2,1001):
        count = 0
        for j in range(1,i+1):
            if(i % j == 0):
                count += 1

        if(count == 2):
            yield i

generator = asal()

for i in generator:
    print(i)