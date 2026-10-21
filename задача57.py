n = int(input())

for _ in range(n):
    line = input()
    
    # Если слово найдено — пропускаем итерацию
    if "плохо" in line:
        continue
        
    # Если слово не найдено, код доходит сюда и выводит строку
    print(line)