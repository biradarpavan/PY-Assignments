from menu import Menu
from order import Order
from exceptions import alreadyexception, notfoundexception, quantityexception

def main():
    menu = Menu()
    order = Order()

    while True:
        print("\nRestaurant Management System")
        print("1. Add Menu Item")
        print("2. Update Menu Item")
        print("3. Delete Menu Item")
        print("4. Display Menu")
        print("5. Take Order")
        print("6. Generate Receipt")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            try:
                menu.add_item(name, price, quantity)
                print(f"Item '{name}' added")
            except alreadyexception as e:
                print(e)

        elif choice == '2':
            name = input("Enter item name to update: ")
            price = float(input("Enter new item price: "))
            quantity = int(input("Enter new item quantity: "))
            try:
                menu.update_item(name, price, quantity)
                print(f"Item '{name}' updated")
            except notfoundexception as e:
                print(e)

        elif choice == '3':
            name = input("Enter item name to delete: ")
            try:
                menu.delete_item(name)
                print(f"Item '{name}' deleted")
            except notfoundexception as e:
                print(e)

        elif choice == '4':
            menu.display_menu()

        elif choice == '5':
            name = input("Enter item name to order: ")
            quantity = int(input("Enter quantity: "))
            try:
                order.add_item(menu, name, quantity)
                print(f"Item '{name}' ordered")
            except (notfoundexception, quantityexception) as e:
                print(e)

        elif choice == '6':
            print(order.generate_receipt())

        elif choice == '7':
            print('Exiting !!!')
            break

        else:
            print("Invalid choice")


main()
