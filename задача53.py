line_number = 0
cat_line = -1  # По умолчанию -1, если кот не найден

while True:
    line = input()
    line_number += 1
    
    if line == "СТОП":
        break
        
    if "кот" in line or "Кот" in line:
        cat_line = line_number  # Запоминаем номер строки
        break  # Дальше искать нет смысла, нам нужна первая строка

print(cat_line)