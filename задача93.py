n = int(input())
numbers = [int(input()) for _ in range(n)]
sums = []

for i in range(n - 1):
    sums.append(numbers[i] + numbers[i + 1])

print(*sums)
