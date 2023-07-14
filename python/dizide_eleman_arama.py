def dizi_arama(dizi, arama):
    for i in dizi:
        if i == arama:
            return True
    return False

dizii = [1, 2, 3, 4, 5]
arama_i = 3

if dizi_arama(dizii, arama_i):
    print("eleman dizinin içinde yer alıyor!")
else:
    print("eleman dizide bulunmuyor.")


