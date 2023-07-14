def dizi_toplam(dizi):
    i = 0
    toplam = 0
    
    while i < len(dizi):
        toplam += dizi[i]
        i += 1
    
    return toplam
dizii = [1, 2, 3, 4, 5]
sonuc = dizi_toplam(dizii)
print(sonuc)
