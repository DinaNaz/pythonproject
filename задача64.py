m = int(input())
english = set()
for _ in range(m):
    english.add(input().strip())

n = int(input())
german = set()
for _ in range(n):
    german.add(input().strip())

only_english = english - german
only_german = german - english
only_one = only_english | only_german

if only_one:
    print(len(only_one))
else:
    print("NO")