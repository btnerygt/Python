def buyuk_kucuk(dizi):
    min_sayi = dizi[0]  
    max_sayi = dizi[0] 
    
    for sayi in dizi[1:]:
        if sayi < min_sayi:
            min_sayi = sayi
        if sayi > max_sayi:
            max_sayi = sayi
    
    return min_sayi, max_sayi

sayilar = [5, 2, 9, 1, 7, 3]
min_sayi, max_sayi = buyuk_kucuk(sayilar)
print("Minimum sayı:", min_sayi)
print("Maximum sayı:", max_sayi)
