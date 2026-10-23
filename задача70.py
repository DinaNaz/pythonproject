set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

sym_diff = set1 ^ set2

if sym_diff:
    print(*sorted(sym_diff))
else:
    print("EMPTY")