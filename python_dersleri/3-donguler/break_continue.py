i = 0

while i < 10:
    print("i:", i)
    i += 1

print("----------------------")
i = 0

while i < 10:
    if i == 5:
        break       # break gördüğü an döngüden çıkar
    print("i:", i)
    i += 1

print("----------------------")
i = 0

while i < 10:
    i += 1
    if i == 5:
        continue        # continue gördüğü zaman döngü bloğu başına döner
    print("i:",i)
    