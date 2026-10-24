username = input()
allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

is_valid = True
for char in username:
    if char not in allowed_chars:
        print(f"Неверный символ: {char}")
        is_valid = False
        break

if is_valid:
    print("OK")