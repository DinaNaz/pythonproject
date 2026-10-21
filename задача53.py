line_number = 0
cat_line = -1  

while True:
    line = input()
    line_number += 1
    
    if line == "СТОП":
        break
        
    if "кот" in line or "Кот" in line:
        cat_line = line_number  
        break  

print(cat_line)