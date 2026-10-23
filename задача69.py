m = int(input())
available_dishes = set()
for _ in range(m):
    available_dishes.add(input().strip())

n = int(input())
cooked_dishes = set()

for _ in range(n):
    daily_dishes = input().strip().split()
    cooked_dishes.update(daily_dishes)

never_cooked = available_dishes - cooked_dishes

for dish in never_cooked:
    print(dish)