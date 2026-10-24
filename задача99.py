white_list = set()
while True:
    line = input()
    if line == "":
        break
    white_list.add(line)

while True:
    line = input()
    if line == "":
        break
    if line in white_list:
        print(line)
