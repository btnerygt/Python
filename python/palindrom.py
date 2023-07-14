def palindrom(sayi):

    sayi_str = str(sayi)

    ters_str = sayi_str[::-1]

    
    if sayi_str == ters_str:
        print("bu sayı palindromdur.")
        return True
    else:
        print("bu sayı palindrom değildir.")
        return False

sayi = int(input("Bir sayı giriniz: "))
print(palindrom(sayi))  