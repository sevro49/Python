"""
Iterator nedir?
for döngülerinde, list comprehensionlarda, generatorlarda karşımıza çıkar

en genel tanımıyla üzerinde gezinilebilecek bir ojbedir ve her seferinde bir tane eleman döner.

Pythonda kendisinden iterator oluşturabileceğimiz her obje iterable bir objedir. Örneğin, demetlerden, listelerden ve stringlerden
oluşturduğumuz bütün objeler iterable bir objedir.

bir objenin iterable olması için hazır metotlar olan __iter()__ ve __next()__ metotlarını mutlaka tanımlaması gerekir.
"""

liste = [1,2,3,4,5]

iterator = iter(liste)
#print(iterator)
# print(next(iterator)) # teker teker eleman bastırır.

#kendi iterator objemizi oluşturma. 
class Kumanda():
    def __init__(self, kanalListesi):
        self.kanalListesi = kanalListesi
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.kanalListesi):
            return self.kanalListesi[self.index]

        else:
            self.index = -1
            raise StopIteration

kumanda = Kumanda(["ATV", "TRT", "FOX", "KanalD", "Bloomberg"])
iterator = iter(kumanda)


print("-----------")

for i in kumanda:
    print(i)