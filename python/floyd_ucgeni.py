def floyd_ucgeni(satir):
    sayi = 1 
    for i in range(1, satir + 1):
        for j in range(1, i + 1):
            print(sayi, end=" ")
            sayi += 1
        print()

sayii = int(input("floyd üçgenin kaç satır olsun: "))
floyd_ucgeni(sayii)
