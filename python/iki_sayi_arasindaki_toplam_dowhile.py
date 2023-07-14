sayi1 = int(input("1. sayı: "))
sayi2 = int(input("2. sayı: "))

if sayi1 > sayi2:
    sayi1, sayi2 = sayi2, sayi1

toplam = 0
gecici = sayi1
while gecici <= sayi2:
    toplam += gecici
    gecici += 1

print( sayi1, "ve", sayi2, "arasındaki sayıların toplamı:", toplam)