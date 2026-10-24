alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
shift = int(input())
text = input()
result = ""
for char in text:
    if char in alphabet:
        old_index = alphabet.find(char)
        new_index = (old_index + shift) % len(alphabet)
        result += alphabet[new_index]
    elif char.lower() in alphabet:
        old_index = alphabet.find(char.lower())
        new_index = (old_index + shift) % len(alphabet)
        result += alphabet[new_index].upper()
    else:
        result += char
print(result)