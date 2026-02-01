user_number_str = input("Please enter a number: ")
user_number = int(user_number_str)

print(f"Counting by 2s up to {user_number}, starting from 1:")
for i in range(1, user_number + 1, 2):
    print(i)
