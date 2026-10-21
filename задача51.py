n = int(input())
found = False

for _ in range(n):
    line = input()
    if "кот" in line or "Кот" in line:
        found = True
        break  # Дальше проверять строки нет смысла

if found:
    print("МЯУ")
else:
    print("НЕТ")