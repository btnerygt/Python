def fibonacci(n):
    # Check if the input is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("girilen veri pozitif ve tam sayı olmalı.")
    
    # Handle the base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize the first two Fibonacci numbers
    sayi1 = 0
    sayi2 = 1
    
    # Calculate subsequent Fibonacci numbers
    for _ in range(2, n+1):
        sayi1, sayi2 = sayi2, sayi1 + sayi2
    
    return sayi2
sayi = int(input("kaçıncı değeri öğrenmek istersin: "))
print("fibonaccinin",sayi,". değeri :",fibonacci(sayi))  