num_str = input().replace("-", "")
digit_sum = 0

for digit in num_str:
    digit_sum += int(digit)

print(digit_sum)
