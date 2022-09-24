"""
"Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. 
Bu sınıfın init fonksiyonu maksimum isimli bir tane parametre alsın
ve her next işleminde ekrana üzerinde bulunduğunuz sayının karesi yazdırılsın. 
StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın.
"""

class Kareler():
    def __init__(self, maksimum):
        self.maksimum = maksimum
        self.kuvvet = 1

    def __iter__(self):
        return self

    def __next__(self):
        if(self.kuvvet <= self.maksimum):
            sonuc = self.kuvvet ** 2

            self.kuvvet += 1

            return sonuc

        else:
            raise StopIteration

kare = Kareler(5)
iterator = iter(kare)

for i in iterator:
    print(i)