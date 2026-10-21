summa = 0
count = 0
steps_to_ten = -1  # По умолчанию -1, если сумма так и не станет 10

while True:
    num = int(input())
    
    if num == 0:
        break
        
    count += 1  # Считаем каждое введенное число
    summa += num
    
    # Проверяем, стала ли сумма равна 10 ВПЕРВЫЕ
    if summa == 10 and steps_to_ten == -1:
        steps_to_ten = count

print(steps_to_ten)