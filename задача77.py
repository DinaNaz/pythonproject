text = input()
codes = [str(ord(char)) for char in text]
print(", ".join(codes))