"""dosya açmak için open() fonksiyonunu kullanıyoruz

open(dosya_adi, dosya_erişme_kipi)"""

#'w' (write) dosya kipi. Dosya oluşturmak istediğimiz dizinde öyle bir dosya yoksa dosya olurşturur.
# Varsa o dosyayı silip tekrar oluşturur. (biraz tehlikelidir.)

file = open("bilgiler.txt", "w")

#işimiz bittiği zaman dosyalarımızı kapatmamız gerekiyor. Kendiliğinden kapanamayabilir. file.close()

file = open("C:/Users/Emre Güler/Desktop/Emre.txt","w")
file.write("Emre Güler")
file.close()


#'a' (append) dosya kipi. mevcut dosyayı silmez. Sonuna ekleme yapar.

file = open("C:/Users/Emre Güler/Desktop/Emre.txt","a")
file.write("\ndeneme123445")
file.close()