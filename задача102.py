n = int(input())
pairs = [input() for _ in range(n)]

for pair in pairs:
    print(pair)

print()

for pair in pairs:
    name, grade = pair.split()
    if grade in ('4', '5'):
        print(pair)
