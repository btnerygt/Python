sayi1 = int(input("1. sayı: "))
sayi2 = int(input("2. sayı: "))

toplam = 0
for sayi in range(sayi1, sayi2+1):
    print(sayi)
    toplam += sayi

print(sayi1, "ve", sayi2, "arasındaki sayıların toplamı:", toplam)
