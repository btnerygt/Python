def pascal_ucgeni(sayi_satiri):
    ucgen = []
    
    for satir in range(sayi_satiri):
        gecici_satir = []
        
        for sutun in range(satir + 1):
            if sutun == 0 or sutun == satir:
                gecici_satir.append(1)
            else:
                onceki = ucgen[satir - 1]
                gecici_satir.append(onceki[sutun - 1] + onceki[sutun])
        
        ucgen.append(gecici_satir)
    
    return ucgen


satirlar  = int(input("Pascal üçgeni kaç satır olsun: "))
pascal_ucgen = pascal_ucgeni(satirlar)

# Print the Pascal's ucgen
for satir in pascal_ucgen:
    print(satir)
