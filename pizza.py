total_cost = float(input("Welcome to the pizza shop! Please enter the total cost of your order: "))

# Calculate 13% tax on that total.
tax_rate = 0.13
tax_amount = total_cost * tax_rate

# Calculate the total amount including tax.
total_amount = total_cost + tax_amount

# Print the total amount including tax.
print(f"Subtotal: ${total_cost:.2f}")
print(f"Tax (13%): ${tax_amount:.2f}")
print(f"Total Amount Due: ${total_amount:.2f}")

