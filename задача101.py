n = int(input())
numbers = [int(input()) for _ in range(n)]

target = numbers[-1]
candidates = numbers[:-1]
found = False

for i in range(len(candidates)):
    for j in range(i + 1, len(candidates)):
        if candidates[i] * candidates[j] == target:
            found = True
            break
    if found:
        break

print("ДА" if found else "НЕТ")
