sozluk1 = {"bir":1,"iki":2,"üç":3,"dört":4} # Anahtar kelimeler ile sözlüğe ulaşılır. freedom = özgürlük demek gibi düşünülebilir. Bir = 1, İki = 2 ...
print("1-",type(sozluk1)) # sozluk1'in tipini ekrana verir.

sozluk2 = {} # boş sözlük.
print("2-",sozluk2)
sozluk2 = dict() # boş sözlük.
print("3-",sozluk2)

print("4-",sozluk1)
print("5-",sozluk1["bir"])

sozluk1["beş"] = 5 # sözlüğe dinamik olarak eleman ekleme işlemi.
print("6-",sozluk1)

sozluk3 = {"bir" : [1,2,3,4], "iki" : [[1,2],[3,4],[5,6]], "üç" : 15}
print("7-",sozluk3["bir"])
print("8-",sozluk3["iki"][1]) # iki anahtar kelimesinin 1. indexine ulaştık.

sozluk1["beş"] = 10 # sözlük içindeki değerler dinamik olarak değiştirilebilir.
print("9-",sozluk1)
sozluk1["beş"] += 1 # sözlük içindeki değerler dinamik olarak toplanabilir, çıkarılabilir.
print("10-",sozluk1)

sozluk4 = {"sayılar":{"bir":1,"iki":2,"üç":3}, "meyveler":{"kiraz":"yaz","portakal":"kış","erik":"yaz"}} # sözlük içinde sözlük oluşturulabilir.
print("11-",sozluk4["sayılar"])
print("12-",sozluk4["sayılar"]["iki"])

print("13-",sozluk1.values()) # sözlük içindeki değerler ekrana bastırılır.
print("14-",sozluk1.keys()) # sözlük içideki anahtar kelimeler ekrana bastırılır.
print("15-",sozluk1.items()) # sözlük içindeki elemanlar demet olarak bastırılır.