summa = 0
count = 0
steps_to_ten = -1 

while True:
    num = int(input())
    
    if num == 0:
        break
        
    count += 1  
    summa += num
  
    if summa == 10 and steps_to_ten == -1:
        steps_to_ten = count

print(steps_to_ten)