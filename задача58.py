cat_found = False

while True:
    line = input()
    
    if line == "СТОП":
        break
        
    if "кот" in line or "Кот" in line:
        cat_found = True
        
    if "пёс" in line or "Пёс" in line:
        cat_found = False

if cat_found:
    print("МЯУ")
else:
    print("НЕТ")