print(*range(10, 20), sep=", ")

print(list(range(10, 20)), sep=", ")
print(*range(10))
print(*range(1, 100, 2))  # (baş, son, atlama değeri)
print(*range(20,0,-1)) # tersten yazdırmak için
"""
for i in range(1,101,2):
    print(i)
"""

for i in range(10):
    print("* "* i)

print(*range(2,6))