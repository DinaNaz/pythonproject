n = int(input())
numbers = [int(input()) for _ in range(n)]

unique_numbers = set(numbers)
print(len(unique_numbers))
