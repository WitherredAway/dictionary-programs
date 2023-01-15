"""Program to calculate the total price of all the fruits in user's shopping cart"""

prices = {'Apple': 3, 'Banana': 5, 'Orange': 6, 'Mango': 10}

shopping_cart = {'Apple': 0, 'Banana': 0, 'Orange': 0, 'Mango': 0}

for fruit in shopping_cart:
    quantity = int(input(f"How many {fruit}{'es' if fruit.lower() == 'mango' else 's'}?: "))
    shopping_cart[fruit] += quantity

total_cost = 0
for fruit, quantity in shopping_cart.items():
    price = prices[fruit] * quantity
    total_cost += price
    print(f"{fruit}: ₹{price}")

print(f"Total cost is ₹{total_cost}")