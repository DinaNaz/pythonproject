text = input()
if text.startswith("Не ") or text.startswith("не "):
    print(text[3:])
else:
    print(text)