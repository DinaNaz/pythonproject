n = int(input())
word_dict = {}

for _ in range(n):
    pos, letter = input().split()
    word_dict[int(pos)] = letter

result = [word_dict[i] for i in range(1, n + 1)]
print("".join(result))
