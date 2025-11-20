from .dictionary import add_inventory, remove_inventory_widget


def display_menu():
    print("Inventory Menu")
    print("1-Add or Update Item")
    print("2-Delete Item")
    print("3-Exit")


def main():
    inventory = {}

    while True:
        display_menu()
        choice = input("Enter option: ").strip()

        if choice == "1":
            name = input("Enter item name: ").strip()
            qty_str = input("Enter quantity to add (can be negative): ").strip()

            try:
                qty = int(qty_str)
            except ValueError:
                print("Quantity must be an integer.\n")
                continue

            add_inventory(inventory, name, qty)
            print(f"{name} now has quantity: {inventory[name]}\n")

        elif choice == "2":
            name = input("Enter item name to delete: ").strip()
            message = remove_inventory_widget(inventory, name)
            print(message)
            print(f"Current inventory: {inventory}\n")

        elif choice == "3":
            print("Exiting Inventory Menu. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
