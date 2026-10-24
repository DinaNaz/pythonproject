text = input()
max_len = 0
current_len = 1

if text:
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
            current_len = 1
            
    if current_len > max_len:
        max_len = current_len

print(max_len)