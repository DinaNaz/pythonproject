n = int(input())
total = 0

for i in range(1, n + 1):
    num = int(input())
    if i % 2 != 0:  # Если номер числа нечетный (1, 3, 5...)
        total += num
    else:           # Если номер числа четный (2, 4, 6...)
        total -= num

print(total)