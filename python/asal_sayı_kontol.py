import math

def asal(sayi):
    if sayi < 2:
        return False

    for i in range(2, int(math.sqrt(sayi)) + 1):
        if sayi % i == 0:
            return False

    return True
sayii = int(input("Bir sayı giriniz: "))
if asal(sayii):
    print(sayii, "sayısı asal sayıdır...")
else:
    print(sayii, "sayısı asal sayı değildir...")
