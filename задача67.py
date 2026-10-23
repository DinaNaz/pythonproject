n = int(input())
counts = {}

for _ in range(n):
    surname = input().strip()
    if surname in counts:
        counts[surname] += 1
    else:
        counts[surname] = 1

count = 0
for value in counts.values():
    if value > 1:
        count += value

print(count)