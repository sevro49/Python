def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True

# bütün değerler True ise True, an az biri False ise False döndürmek istiyoruz.
print(hepsi([1,2,3,4,5,6]))


def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False

# Herhangi bir değer True ise True, Hepsi False ise False döndürür

print(herhangi([1,2,3,4,5,6,7,7,8,0]))

#aslında bu işlemleri all() ve any() fonksiyonları yapmaktadır.

print(all([1,2,3,0]))
print(any([1,2,3,4,5,0]))