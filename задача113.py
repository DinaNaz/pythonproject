n = int(input())
strings = [input() for _ in range(n)]

for s in strings:
    t = (len(s), s)
    print(t)
