# upper() fonksiyonu, içine girilen değeri büyük harfe çevirir
# lower() metodu, içine girilen değeri küçük harfe çevirir.

print("emrE".upper())
print("SDFEfdER".lower())


# replace(x,y) metodu, stringdeki x değerlerini y ile değiştirir
print("Herkes ana baba bacı gardaş".replace("a", "o"))
print("Python Programlama Dili".replace(" ", "-"))


# startswith(x): string x ile başlıyorsa True, başlamıyorsa False döndürür.
# endswith(x): string x ile bitiyorsa True, bitmiyorsa False değeri döndürür.

print("Emre".startswith("E"))
print("Emre".endswith("e"))
print("Zeynep".startswith("z"))
print("Zeynep".endswith("P"))


# split(a): verilen bir a değerine göre stringi parçalara ayırarak herbir parça listeye atılır.

liste = "Python Programlama Dili".split(" ") # boşluk karakterine göre ayrıldı.
print(liste)

liste = "Python Programlama Dili".split("l")  # l harfine göre ayrıldı.
print(liste)


#strip(x): stringin başında ve sonunda bulunan x değerlerini siler.
#lstrip(x): stringin sadece başında bulunan x değerlerini siler.
#rstrip(x): stringin sadece sonunda bulunan x değerlerini siler.

print("            emre               ".strip()) # değer göndermezsek varsayılan olarak boşluğu siler
print(">>>>>>>>>>>>>>>>Zeynep>>>>>>>>".strip(">"))
print(">>>>>>>>>>>>>>>>Zeynep>>>>>>>>".lstrip(">"))
print(">>>>>>>>>>>>>>>>Zeynep>>>>>>>>".rstrip(">"))


# join(): listenin elemanlarını bir string değeriyle birleştirmemizi sağlar

liste = ["18","12","2000"]
print("/".join(liste))

liste = ["T","B","M","M"]
print(".".join(liste))


# count(x): string içindeki x değerlerini sayar.
# count(x, index): stringin içindeki x değerlerini verilen index değerinden başlayarak saymaya başlar.
print("Emre".count("E"))
print("Zeynep".count("e"))
print("Zeynep".count("e",2))


#find(x): x değerini baştan itibaren string içinde arar ve bulursa bulduğu ilk indexi döndürür. Bulamazsa -1 döndürür
#rfind(x): x değerini sağdan itibaren string içinde arar ve bulursa bulduğu ilk indexi döndürür. Bulamazsa -1 döndürür

print("Zeynep".find("e"))
print("Zeynep".rfind("e"))
print("Zeynep".find("E"))