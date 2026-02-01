bill_amount = float(input("Please enter the total bill amount: "))

tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

tip_amount = bill_amount * (tip_percentage / 100)

total_bill = bill_amount + tip_amount

print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total bill with tip: ${total_bill:.2f}")
