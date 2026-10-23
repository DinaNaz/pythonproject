m = int(input())
fridge = set()
for _ in range(m):
    fridge.add(input().strip().lower())

n = int(input())
found_recipes = []

for _ in range(n):
    recipe_line = input().strip().split()
    if not recipe_line:
        continue
    
    recipe_name = recipe_line[0]
    ingredients = set(item.lower() for item in recipe_line[1:])
    
    if ingredients.issubset(fridge):
        found_recipes.append(recipe_name)

for recipe in found_recipes:
    print(recipe)