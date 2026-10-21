line_number = 0
cat_count = 0
first_cat_line = -1  

while True:
    line = input()
    
    if line == "СТОП":
        break
        
    line_number += 1  
    
    if "кот" in line or "Кот" in line:
        cat_count += 1 
        
     
        if first_cat_line == -1:
            first_cat_line = line_number

print(cat_count)
print(first_cat_line)