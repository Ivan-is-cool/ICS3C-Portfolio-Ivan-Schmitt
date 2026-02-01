target_number = int(input("Enter a number to count to: "))
step_amount = int(input("Enter the step amount: "))

for i in range(0, target_number + 1, step_amount):
    print(i)

print("Blast off!")
