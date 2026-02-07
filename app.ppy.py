store_items = [
    {"name": "Apple", "price": 1.25, "category": "Fruit"},
    {"name": "Bread", "price": 2.50, "category": "Bakery"},
    {"name": "Milk", "price": 3.00, "category": "Dairy"}
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
