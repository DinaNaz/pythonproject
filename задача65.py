m = int(input())
home_library = set()
for _ in range(m):
    home_library.add(input().strip())

n = int(input())
for _ in range(n):
    book = input().strip()
    if book in home_library:
        print("YES")
    else:
        print("NO")