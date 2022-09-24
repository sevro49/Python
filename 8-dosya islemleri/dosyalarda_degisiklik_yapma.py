"""with open("C:/Users/Emre Güler/Desktop/Emre.txt","r+") as file: # r+ hem okumaya hem yazmaya yarar
    print(file.read())"""


"""with open("C:/Users/Emre Güler/Desktop/Emre.txt","r+") as file: 
    file.seek(0)
    
    
with open("C:/Users/Emre Güler/Desktop/Emre.txt","r+") as file: 
    print(file.read())"""

# Dosya sonunda değişiklik yapmak
with open("C:/Users/Emre Güler/Desktop/Emre.txt","a") as file:
    file.write("Lionel Messi\n")

with open("C:/Users/Emre Güler/Desktop/Emre.txt","r") as file:
    print(file.read())

# Dosya başında değişiklik yapmak
with open("C:/Users/Emre Güler/Desktop/Emre.txt","r+") as file:
    icerik = file.read()
    icerik = "SIUUUUUUUUUUU\n" + icerik
    print(icerik)

#dosya ortasında değişiklik yapmak

with open("C:/Users/Emre Güler/Desktop/Emre.txt","r+") as file:
    liste = file.readlines()
    print(liste)

with open("C:/Users/Emre Güler/Desktop/Emre.txt","r+") as file:
    liste = file.readlines()
    liste.insert(3, "AAAAAAAAAAAAAAAAAA\n")
    file.seek(0)

    for i in liste:
        print(i, end="")

