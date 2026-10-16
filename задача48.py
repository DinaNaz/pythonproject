n = int(input())
product = 1

for _ in range(n):
    num = int(input())
    if num != 0:
        product *= num

print(product)