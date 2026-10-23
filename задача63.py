def read_list():
    numbers = []
    seen = set()
    while True:
        try:
            line = input().strip()
            if not line:
                break
            num = int(line)
            if num not in seen:
                numbers.append(num)
                seen.add(num)
        except EOFError:
            break
    return numbers, seen

list1, set1 = read_list()
list2, set2 = read_list()

common_elements = set1 & set2

if common_elements:
    result = [str(num) for num in list1 if num in common_elements]
    print(" ".join(result))
else:
    print("EMPTY")