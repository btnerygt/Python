aralik = range(1, 11)  # 1 den 10'a kadar olan sayıların çarpımı

for i in aralik:
    for j in aralik:
        result = i * j
        print(f"{i} x {j} = {result}")
    print()
