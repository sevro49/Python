import string

class myString(str):
    def __init__(self):
        pass

    def append(self, str):
        string = ""
        string += str
        print(string)


s = myString()
s.append("Emre")
s.append("Güler")
s.append("Zeynep")
print(s)

