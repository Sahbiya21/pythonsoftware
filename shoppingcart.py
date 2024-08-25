class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, name, price, quantity):
        if name in self.cart:
            self.cart[name]['quantity'] += quantity
        else:
            self.cart[name] = {'price': price, 'quantity': quantity}

    def remove_item(self, name):
        if name in self.cart:
            del self.cart[name]
        else:
            print("Item not found in cart.")

    def update_quantity(self, name, quantity):
        if name in self.cart:
            self.cart[name]['quantity'] = quantity
        else:
            print("Item not found in cart.")

    def view_cart(self):
        print("Shopping Cart:")
        for item, details in self.cart.items():
            print(f"Item: {item}, Price: {details['price']}, Quantity: {details['quantity']}")

    def calculate_total(self):
        total = sum(details['price'] * details['quantity'] for details in self.cart.values())
        return total


cart = ShoppingCart()

while True:
    print("\n1. Add item to cart")
    print("2. Remove item from cart")
    print("3. Update item quantity")
    print("4. View cart")
    print("5. Calculate total")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        cart.add_item(name, price, quantity)
    elif choice == "2":
        name = input("Enter item name: ")
        cart.remove_item(name)
    elif choice == "3":
        name = input("Enter item name: ")
        quantity = int(input("Enter new quantity: "))
        cart.update_quantity(name, quantity)
    elif choice == "4":
        cart.view_cart()
    elif choice == "5":
        print("Total:", cart.calculate_total())
    elif choice == "6":
        break
    else:
        print("Invalid option. Please choose a valid option.")