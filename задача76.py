message = input()
n = int(input())
if 1 <= n <= len(message):
    print(message[n - 1])
else:
    print("ОШИБКА")