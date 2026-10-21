a = int(input())
b = int(input())

result = []

for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0:
        result.append("FizzBuzz")
    elif i % 3 == 0:
        result.append("Fizz")
    elif i % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(i))  # Числа нужно превратить в строку для вывода

# Выводим все элементы списка через пробел
print(*result)