import math

a = float(input("Üçgenin kenarını giriniz a: "))
b = float(input("Üçgenin kenarını giriniz b: "))
c = float(input("Üçgenin kenarını giriniz c: "))
taban = float(input("üçgenin tabanı: "))
yukseklik = float(input("Yukseklik: "))

cevre = a + b + c

alan = (taban * yukseklik) / 2;

print("alan:", alan)
print("cevre:", cevre)
