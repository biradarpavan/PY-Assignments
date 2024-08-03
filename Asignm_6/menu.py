from exceptions import alreadyexception, notfoundexception

class MenuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name},{self.price},{self.quantity}"

class Menu:
    def __init__(self):
        self.menu_items = []
        self.read_menu_from_file()

    def add_item(self, name, price, quantity):
        for item in self.menu_items:
            if item.name == name:
                raise alreadyexception(f"Item '{name}' already exists in the menu.")
        new_item = MenuItem(name, price, quantity)
        self.menu_items.append(new_item)
        self.write_menu_to_file()

    def update_item(self, name, price, quantity):
        for item in self.menu_items:
            if item.name == name:
                item.price = price
                item.quantity = quantity
                self.write_menu_to_file()
                return
        raise notfoundexception(f"Item '{name}' not found in the menu.")

    def delete_item(self, name):
        for item in self.menu_items:
            if item.name == name:
                self.menu_items.remove(item)
                self.write_menu_to_file()
                return
        raise notfoundexception(f"Item '{name}' not found in the menu.")

    def display_menu(self):
        if not self.menu_items:
            print("Menu is empty.")
        else:
            for item in self.menu_items:
                print(f"Name: {item.name}, Price: {item.price}, Quantity: {item.quantity}")

    def read_menu_from_file(self):
        try:
            file = open('menu.txt','r')
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name, price, quantity = parts
                    self.menu_items.append(MenuItem(name, float(price), int(quantity)))
        except FileNotFoundError as e:
            print(e)

    def write_menu_to_file(self):
        file = open('menu.txt', 'r+')
        for item in self.menu_items:
            file.write(str(item) + '\n')

