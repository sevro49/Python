"""1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın. 
Daha sonra bir tane decorator fonksiyon kullanarak bu fonksiyona 1'den 1000'e kadar olan mükemmel sayıları yazdırma özelliği ekleyin."""

def mukemmel(func):
    def wrapper():
        liste = list()

        for i in range(2,1001):
            toplam = 0
            for j in range(1,i):
                if(i % j == 0):
                    toplam += j

            if(i == toplam):
                liste.append(i)

        print("mükemmel sayılar:" ,liste)
        
        func()

    return wrapper
                    
@mukemmel
def asal():
    liste = list()
    

    for i in range(2, 1001):
        count = 0
        for j in range(1,i+1):
            if(i % j == 0):
                count += 1
                
        
        if(count == 2):
            liste.append(i)

    print("asal sayılar:",liste)

asal()

