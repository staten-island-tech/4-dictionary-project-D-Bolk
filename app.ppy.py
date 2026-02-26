store_items = [
    {"name": "Apple", "price": 1.25, "category": "Fruit"},
    {"name": "Bread", "price": 2.50, "category": "Bakery"},
    {"name": "Milk", "price": 3.00, "category": "Dairy"},
    {"name": "Strawberries", "price": 2.99, "category": "Fruit"},
    {"name": "Blueberries", "price": 3.49, "category": "Fruit"},
    {"name": "Spinach", "price": 1.99, "category": "Vegetable"},
    {"name": "Broccoli", "price": 2.29, "category": "Vegetable"},
    {"name": "Salmon", "price": 8.99, "category": "Seafood"},
    {"name": "Ground Beef", "price": 6.49, "category": "Meat"},
    {"name": "Yogurt", "price": 1.19, "category": "Dairy"},
    {"name": "Cheddar Cheese", "price": 4.79, "category": "Dairy"},
    {"name": "Butter", "price": 3.59, "category": "Dairy"},
    {"name": "Bagels", "price": 3.99, "category": "Bakery"},
    {"name": "Croissant", "price": 2.49, "category": "Bakery"},
    {"name": "Rice", "price": 2.89, "category": "Grains"},
    {"name": "Pasta", "price": 1.79, "category": "Grains"},
    {"name": "Cereal", "price": 4.29, "category": "Breakfast"},
    {"name": "Coffee", "price": 7.99, "category": "Beverage"},
    {"name": "Tea", "price": 3.49, "category": "Beverage"},
    {"name": "Soda", "price": 1.25, "category": "Beverage"},
    {"name": "Chips", "price": 2.99, "category": "Snack"},
    {"name": "Chocolate", "price": 1.99, "category": "Snack"},
    {"name": "Ice Cream", "price": 5.49, "category": "Frozen"}
]

cart = []
shopping = True

while shopping:
    print("\nStore Items:")
    for item in store_items:
        print(item["name"])

    choice = int(input("Enter the index of the item you want to purchase: "))
    cart.append(store_items[choice])

    keep_shopping = input("Do you want to continue shopping? (yes/no): ").lower()
    if keep_shopping != "yes":
        shopping = False

print("\nItems purchased:")
total = 0

for item in cart:
    print(item["name"])
    total += item["price"]

print(f"Total cost: ${total:.2f}")
