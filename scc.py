import tkinter as tk
from tkinter import messagebox

class ShoppingCart:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Cart")
        self.root.configure(bg="#F0F0F0")
        self.cart = {}
        self.items = {
            "Apple": 1.00,
            "Banana": 0.50,
            "Orange": 1.50,
            "Milk": 2.00,
            "Bread": 1.25,
            "Eggs": 1.75
        }
        self.create_widgets()

    def create_widgets(self):
        # Create frames
        self.frame1 = tk.Frame(self.root, bg="#F0F0F0")
        self.frame2 = tk.Frame(self.root, bg="#F0F0F0")
        self.frame3 = tk.Frame(self.root, bg="#F0F0F0")

        # Frame 1
        tk.Label(self.frame1, text="Select Item:", bg="#F0F0F0").pack(side=tk.LEFT)
        self.item_var = tk.StringVar()
        self.item_menu = tk.OptionMenu(self.frame1, self.item_var, *self.items.keys())
        self.item_menu.pack(side=tk.LEFT)
        tk.Label(self.frame1, text="Quantity:", bg="#F0F0F0").pack(side=tk.LEFT)
        self.quantity_entry = tk.Entry(self.frame1)
        self.quantity_entry.pack(side=tk.LEFT)
        tk.Button(self.frame1, text="Add to Cart", command=self.add_item, bg="#ADD8E6").pack(side=tk.LEFT)

        # Frame 2
        tk.Button(self.frame2, text="View Cart", command=self.view_cart, bg="#ADD8E6").pack(side=tk.LEFT)
        tk.Button(self.frame2, text="Calculate Total", command=self.calculate_total, bg="#ADD8E6").pack(side=tk.LEFT)

        # Frame 3
        self.cart_text = tk.Text(self.frame3)
        self.cart_text.pack()

        # Pack frames
        self.frame1.pack(pady=10)
        self.frame2.pack(pady=10)
        self.frame3.pack(pady=10)

    def add_item(self):
        item = self.item_var.get()
        price = self.items[item]
        quantity = int(self.quantity_entry.get())
        self.cart[item] = {'price': price, 'quantity': quantity}
        self.quantity_entry.delete(0, tk.END)

    def view_cart(self):
        self.cart_text.delete(1.0, tk.END)
        for item, details in self.cart.items():
            self.cart_text.insert(tk.END, f"Item: {item}, Price: {details['price']}, Quantity: {details['quantity']}\n")

    def calculate_total(self):
        total = sum(details['price'] * details['quantity'] for details in self.cart.values())
        messagebox.showinfo("Total", f"Total: {total}")

root = tk.Tk()
cart = ShoppingCart(root)
root.mainloop()

