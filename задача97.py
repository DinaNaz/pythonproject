n = int(input())
strings = [input() for _ in range(n)]
word1 = input()
word2 = input()

for s in strings:
    if word1 in s and word2 in s:
        print(s)
