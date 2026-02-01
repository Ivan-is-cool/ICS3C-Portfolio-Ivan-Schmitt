age = int(input("Enter your age: "))
has_membership = input("Do you have a membership? (yes/no): ")

if age >= 18 and has_membership == "yes":
    print("You can enter the gym.")

else:
    print("You cannot enter the gym.")
