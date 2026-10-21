line_number = 0
cat_count = 0
first_cat_line = -1  # По умолчанию -1, если кот не найден

while True:
    line = input()
    
    if line == "СТОП":
        break
        
    line_number += 1  # Считаем номер текущей строки
    
    if "кот" in line or "Кот" in line:
        cat_count += 1  # Увеличиваем счетчик строк с котом
        
        # Если это первый найденный кот, запоминаем номер строки
        if first_cat_line == -1:
            first_cat_line = line_number

print(cat_count)
print(first_cat_line)