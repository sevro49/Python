from PIL import Image

image = Image.open("49.png") # göstermek istediğimiz image current workspace içinde olmalı.

image.save("49.2.png")

image.rotate(180).save("49.3.png")

image.convert(mode = "L").save("49.5.png") #fotoyu siyah beyaz hale getirir. 
#image.show()
