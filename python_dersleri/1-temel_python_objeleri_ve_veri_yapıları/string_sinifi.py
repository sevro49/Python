a = 49
print("Yaş:\n", a, "\nTarih:\n", 2022)
print(type(a)) # type() içine girdiğimiz şeyin türünü verir

print(1,2,3,4,5,6) # araya boşluk koyarak yazdırır
print(1,2,3,4,5,6, sep = ", ") # sep içinde ne varsa araya onu koyar

print("Python")
print(*"Python") #karakterler arasına boşluk koyar
print("T","B","M","M", sep = ".")
print(*"TBMM", sep = ".") 

#formatlama

a = 10
b = 11
print("{} + {}'nin toplamı {}'dır".format(a,b,a+b))
print("{1}, {0}, {2}".format("Emre", 20, "Güler")) #indis numarasına göre ekleme yapılır.
print("{:.2f}, {:.3f}".format(23423.345346,345345.545675676)) #virgülden sonraki 2 basamağı ve 3 basamağı alır.