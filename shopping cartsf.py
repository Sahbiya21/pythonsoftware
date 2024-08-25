import tkinter as tk
from tkinter import messagebox

class ShoppingCart:
    def __init__(self, root):
        self.root = root
        self.cart = {}
        self.create_widgets()

    def create_widgets(self):
        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame2 = tk.Frame(self.root)
        self.frame3 = tk.Frame(self.root)

        # Frame 1
        tk.Label(self.frame1, text="Item Name:").pack(side=tk.LEFT)
        self.item_name_entry = tk.Entry(self.frame1)
        self.item_name_entry.pack(side=tk.LEFT)
        tk.Label(self.frame1, text="Price:").pack(side=tk.LEFT)
        self.price_entry = tk.Entry(self.frame1)
        self.price_entry.pack(side=tk.LEFT)
        tk.Label(self.frame1, text="Quantity:").pack(side=tk.LEFT)
        self.quantity_entry = tk.Entry(self.frame1)
        self.quantity_entry.pack(side=tk.LEFT)
        tk.Button(self.frame1, text="Add to Cart", command=self.add_item).pack(side=tk.LEFT)

        # Frame 2
        tk.Button(self.frame2, text="View Cart", command=self.view_cart).pack(side=tk.LEFT)
        tk.Button(self.frame2, text="Calculate Total", command=self.calculate_total).pack(side=tk.LEFT)

        # Frame 3
        self.cart_text = tk.Text(self.frame3)
        self.cart_text.pack()

        # Pack frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

    def add_item(self):
        name = self.item_name_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())
        self.cart[name] = {'price': price, 'quantity': quantity}
        self.item_name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
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