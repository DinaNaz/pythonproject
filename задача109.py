n = int(input())
people = []

for _ in range(n):
    name, height = input().split()
    people.append((name, int(height)))

people.sort(key=lambda x: x[1], reverse=True)

for name, height in people:
    print(f"{name} {height}")
