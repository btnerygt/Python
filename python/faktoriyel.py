def faktoriyel_loop(n):
	sonuc = 1
	for i in range(1, n + 1):
		sonuc *= i
	return sonuc
def faktoriyel_recursive(n):
	if n == 0:
		return 1
	else:
		return n * faktoriyel_recursive(n - 1)

sayi = int(input("Bir sayı giriniz: "))

print("döngüyle:",faktoriyel_loop(sayi))  

print("özyenilemeyle:",faktoriyel_recursive(sayi))  
