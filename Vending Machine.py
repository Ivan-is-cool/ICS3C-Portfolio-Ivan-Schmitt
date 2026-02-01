#The Machine Sells 3 Items
items = {1:("Chips",2.00), 2: ("Chocolate", 2.50), 3:("Soda",3.00)}

print("Vending Machine")
print("1. Chips - $2.00")
print("2. Chocolate - $2.50")
print("3. Soda - $3.00")


choise = int(input("Select an item: "))
price = items[choise][1]

money = float(input("Insert Money: "))

if money < price:
    print("Not enough. Transaction cancelled.")
elif money == price:
    print("enjoy your item!!")
else:
    change = money - price
    print("Enjoy your item! Your change is $",change)
    
