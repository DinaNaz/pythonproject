text = input()
vowels = "аеёиоуыэюя"
count = 0
for char in text:
    if char.lower() in vowels:
        count += 1
print(count)