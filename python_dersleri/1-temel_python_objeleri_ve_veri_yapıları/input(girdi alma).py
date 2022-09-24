#input() # çalıştırdığımız zaman program bizden bir veri girişi yapmamızı ister.
#input("lütfen bir sayı giriniz: ")

"""a = input("lütfen bir sayı giriniz: ") # alınan veriyi daha sonra kullanmak için böyle yapıyoruz.
print("Kullanıcının girdiği değer:",a) """

"""b = input("lütfen bir sayı giriniz: ")
print(b * 3) # b, str tipinde olduğu için 3*b işlemi yapmaz. bbb şeklinde ekrana bastırır.
b = int(input("lütfen bir sayı giriniz: "))
print(b * 3) # b, int tipine dönüştürüldüğü için 3*b işlemi yapılır. """

a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))
c = int(input("Üçüncü sayı: "))
print("Toplam =",a+b+c)

