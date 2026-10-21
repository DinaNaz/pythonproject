total_sum = 0
count = 0

while True:
    num = int(input())

    if num == 0:
        break
        
    total_sum += num
    count += 1
 
    if total_sum > 100:
        print("СТОП")
        print(count)
        break  
else:
   
    print("ОК")