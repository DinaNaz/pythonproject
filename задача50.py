n = int(input())
total = 0

for i in range(1, n + 1):
    num = int(input())
    if i % 2 != 0:  
        total += num
    else:           
        total -= num

print(total)