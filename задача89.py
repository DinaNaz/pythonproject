n = int(input())

for _ in range(n):
    line = input()
    if line.startswith("%%"):
        print(line[2:])
    elif line.startswith("####"):
        continue
    else:
        print(line)