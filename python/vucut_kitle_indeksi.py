kilo = float(input("kilonuz: "))
boy = float(input("boyunuz: "))

indeks = kilo / (boy * boy)

print("Vücut kitle indeksiniz: ", indeks)

if indeks<18.5:
        print("ideal kilonun altinda")
elif indeks>=18.5 and indeks<=24.9 :
    print("ideal kiloda") 
elif indeks>=25 and indeks<=29.9 :
    print("ideal kilonun ustunde") 
elif indeks>=30 and indeks<=39.9 :
    print("ideal kilonun ustunde - obez")  
elif indeks>=40 :
     print("ideal kilonun cok ustunde - morbid obez") 
else:
    print("gecerli degerler giriniz.") 