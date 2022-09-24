# listeden farkı sonradan değiştirilemezler ve parantez kullanılarak gösterilirler!!

demet1 = (1,2,3,4,5,6,7)
print("1-",type(demet1))

print("2-",demet1[2]) # 2. indexe erişilir.
print("3-",demet1[-1]) # son elemana ulaşılır.
print("4-",demet1[:4]) # ilk 4 eleman yazdırılır.
print("5-",demet1[::-1]) # demeti tersten yazdırır.

"""tuple içinde herhangi bir değişiklik yapılmadığı için 2 tane metotları vardır. index ve count
index = verdiğimiz elemanın hangi indexte olduğunu gösterir.
count = verdiğimiz değerin demet içinde kaç defa geçtiğini gösterir.
"""

demet2 = (1,2,3,3,3,4,4,5,6,7,7,7,7)
print("6-",demet2.index(5)) # 5 elemanının bulunduğu indexi verir.
print("7-",demet2.index(3,3)) # 3 elemanından 2 tane olduğu için (3) yazarsak ilk 3'ün indexini, (3,3) yazarsak ikinci 3'ün indexini verir.
print("8-",demet2.count(4)) # 4 elemanının demette kaç defa olduğunu verir.

demet3 = (1,2,3)
#demet3[0] = 10 # demetler değiştirilemediği için bu işlem hata verir.

# sabit değerler kullanırken demetlere ihtiyaç duyulur. Read only tip olduğu için listeden biraz daha hızlı çalışır.

