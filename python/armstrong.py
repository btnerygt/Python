sayi = int(input("Bir sayı giriniz: "))
sayi_str = str(sayi)
basamak_sayisi = len(sayi_str)
sonuc = 0

for basamak in sayi_str:
    sonuc += int(basamak)**basamak_sayisi

if sonuc == sayi:
    print(sayi, "sayısı bir Armstrong sayıdır...")
else:
    print(sayi, "sayısı bir Armstrong sayı değildir...")
