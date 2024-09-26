class MenuItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class Menu:
    def __init__(self):
        self.items = []

    def add_item(self,name,price):
        item = MenuItem(name,price)
        self.items.append(item)
        print(f"{name} added to the menu.")

    def remove_item(self,name):
        self.items = [item for item in self.items if item.name != name]
        print(f"{name} removed from the menu.")

    def display_menu(self):
        if not self.items:
            print("Menu is empty")
        else:
            print("\n--- Menu ---")
            for item in self.items:
                print(f"{item.name}: ${item.price:.2f}")
        print() 

class Order:
    def __init__(self, table_number):
        self.table_number = table_number
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def display_order(self):
        print(f"Order for table {self.table_number}:")
        for item, quantity in self.items:
            print(f"{item.name} x{quantity} - ${item.price * quantity:.2f}")
        print()

class OrderManager:
    def __init__(self):
        self.orders = []

    def place_order(self, table_number, menu):
        order = Order(table_number)
        while True:
            menu.display_menu()
            item_name = input("Enter item name to order (or 'done' to finish): ")
            if item_name.lower() == 'done':
                break
            quantity = int(input("Enter quantity: "))
            item = next((item for item in menu.items if item.name == item_name), None)
            if item:
                order.add_item(item, quantity)
            else:
                print(f"{item_name} not found in menu.")
        self.orders.append(order)
        print(f"Order placed for table {table_number}")

    def view_orders(self):
        if not self.orders:
            print("No current orders.")
        for order in self.orders:
            order.display_order()

class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_reserved = False

class ReservationSystem:
    def __init__(self, num_tables):
        self.tables = [Table(i) for i in range(1, num_tables + 1)]

    def reserve_table(self, table_number):
        if 1 <= table_number <= len(self.tables):
            table = self.tables[table_number - 1]
            if not table.is_reserved:
                table.is_reserved = True
                print(f"Table {table_number} reserved.")
            else:
                print(f"Table {table_number} is already reserved.")
        else:
            print("Invalid table number.")

    def view_available_tables(self):
        available_tables = [table.table_number for table in self.tables if not table.is_reserved]
        if available_tables:
            print(f"Available tables: {', '.join(map(str, available_tables))}")
        else:
            print("No available tables.")
class Billing:
    def generate_bill(self, order):
        total = sum(item.price * quantity for item, quantity in order.items)
        print(f"--- Bill for table {order.table_number} ---")
        for item, quantity in order.items:
            print(f"{item.name} x{quantity}: ${item.price * quantity:.2f}")
        print(f"Total: ${total:.2f}")
        print("Thank you for dining with us!")
        
def main():
    menu = Menu()
    order_manager = OrderManager()
    reservation_system = ReservationSystem(num_tables=10)
    billing = Billing()

    while True:
        print("\n--- Restaurant Management ---")
        print("1. View Menu")
        print("2. Place Order")
        print("3. View Current Orders")
        print("4. Reserve a Table")
        print("5. View Available Tables")
        print("6. Generate Bill")
        print("7. Admin - Add Menu Item")
        print("8. Admin - Remove Menu Item")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            menu.display_menu()
        elif choice == '2':
            table_number = int(input("Enter table number: "))
            order_manager.place_order(table_number, menu)
        elif choice == '3':
            order_manager.view_orders()
        elif choice == '4':
            table_number = int(input("Enter table number to reserve: "))
            reservation_system.reserve_table(table_number)
        elif choice == '5':
            reservation_system.view_available_tables()
        elif choice == '6':
            table_number = int(input("Enter table number for billing: "))
            order = next((order for order in order_manager.orders if order.table_number == table_number), None)
            if order:
                billing.generate_bill(order)
            else:
                print(f"No order found for table {table_number}.")
        elif choice == '7':
            name = input("Enter dish name: ")
            price = float(input("Enter dish price: "))
            menu.add_item(name, price)
        elif choice == '8':
            name = input("Enter dish name to remove: ")
            menu.remove_item(name)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
