from menu import Menu, MenuItem
from exceptions import notfoundexception, quantityexception

class Order:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, menu, name, quantity):
        for item in menu.menu_items:
            if item.name == name:
                if item.quantity >= quantity:
                    self.items.append(MenuItem(name, item.price, quantity))
                    item.quantity -= quantity
                    self.total += item.price * quantity
                    menu.write_menu_to_file()
                    return
                else:
                    raise quantityexception(f"item is outof stock")
        raise notfoundexception(f"Item not found in the menu.")

    def calculate_total(self):
        return self.total

    def generate_receipt(self):
        receipt = "Receipt:\n"
        for item in self.items:
            receipt += f"{item.name} x {item.quantity} = {item.price * item.quantity}\n"
        receipt += f"Total: {self.total}"
        file = open('orders.txt', 'a')
        file.write(receipt + '\n')
        return receipt
