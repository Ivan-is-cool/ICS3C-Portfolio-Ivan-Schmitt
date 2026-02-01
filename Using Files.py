numbers = [1, 2, 3, 4]
file_name = "numbers.txt"

with open(file_name, 'w') as file:
    for number in numbers:
        file.write(str(number) + '\n')

print(f"List of numbers written to {file_name}")
