n = int(input())
text = input()

if len(text) > n:
    print(text[:n-3] + "...")
else:
    print(text)