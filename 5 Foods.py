foods = ["Pizza", "Sushi", "Tacos", "Ice Cream", "Bugurs"]

print("Entire list of foods:", foods)

print("First food:", foods[0])
print("Last food:", foods[-1])

num_foods = len(foods)
print("Number of foods in the list:", num_foods)

print("Foods listed individually:")
for food in foods:
    print(food)

foods.append("Chocolate")
print("List after appending a new food:", foods)
