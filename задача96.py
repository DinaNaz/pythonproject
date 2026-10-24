n = int(input())
numbers = [int(input()) for _ in range(n)]
p = int(input())
q = int(input())

print(sum(numbers[p:q + 1]))
