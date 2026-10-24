n = int(input())
strings = [input() for _ in range(n)]
query = input()

for s in strings:
    if query in s:
        print(s)
