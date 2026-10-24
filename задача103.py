n = int(input())
strings = [input() for _ in range(n)]

for s in sorted(strings):
    print(s)
