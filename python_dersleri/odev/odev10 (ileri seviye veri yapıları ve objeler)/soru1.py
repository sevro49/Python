"""
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.
"""

str = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

def split(word):
    return [char for char in word]

liste = split(str)

harf_sozluk = dict()

for i in liste:
    if(i in harf_sozluk):
        harf_sozluk[i] += 1
    else:
        harf_sozluk[i] = 1

for harf,sayi in harf_sozluk.items():
    print("{} harfi {} defa geçiyor".format(harf,sayi))
    print("----------")