n = int(input())
total_sum = 0

for _ in range(n):
    num = int(input())
    
    if num <= 0:
        continue
        
    total_sum += num

print(total_sum)