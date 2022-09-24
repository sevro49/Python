# and, or, not

print("1-", bool(1 < 2 and "Emre" != "Ahmet")) # True 
print("2-", bool(2 > 4 and 5.4 > 3.0 and "a" == "a")) # False

print("3-", bool(1 > 2 or 2 > 0)) # True
print("4-", bool(1 > 10 or "Emre" == "Ahmet")) # False

print("5-", bool(not 2 == 2)) # False (not tam tersini alır)
print("6-", bool(not 3 != 3))

print("7-", bool(not (2.14 > 3.49 or (2 != 2 and "Emre" == "Emre")))) # True

