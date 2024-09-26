from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Classes from your code
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        item = MenuItem(name, price)
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def get_menu(self):
        return [{'name': item.name, 'price': item.price} for item in self.items]

class Order:
    def __init__(self, table_number):
        self.table_number = table_number
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

class OrderManager:
    def __init__(self):
        self.orders = []

    def place_order(self, table_number, menu_items):
        order = Order(table_number)
        for item_name, quantity in menu_items:
            item = next((item for item in menu.items if item.name == item_name), None)
            if item:
                order.add_item(item, quantity)
        self.orders.append(order)
        return order

    def get_orders(self):
        return [
            {
                'table_number': order.table_number,
                'items': [{'name': item.name, 'quantity': quantity} for item, quantity in order.items]
            }
            for order in self.orders
        ]

class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_reserved = False

class ReservationSystem:
    def __init__(self, num_tables):
        self.tables = [Table(i) for i in range(1, num_tables + 1)]

    def reserve_table(self, table_number):
        table = self.tables[table_number - 1]
        if not table.is_reserved:
            table.is_reserved = True
            return True
        return False

    def get_available_tables(self):
        return [table.table_number for table in self.tables if not table.is_reserved]

class Billing:
    def generate_bill(self, order):
        total = sum(item.price * quantity for item, quantity in order.items)
        bill = {
            'table_number': order.table_number,
            'items': [{'name': item.name, 'quantity': quantity, 'price': item.price * quantity} for item, quantity in order.items],
            'total': total
        }
        return bill

# Initialize systems
menu = Menu()
order_manager = OrderManager()
reservation_system = ReservationSystem(num_tables=10)
billing = Billing()

# Route to serve the index.html file
@app.route('/')
def home():
    return render_template('index.html')

# Routes for Menu
@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu.get_menu())

@app.route('/menu', methods=['POST'])
def add_menu_item():
    data = request.json
    name = data.get('name')
    price = data.get('price')
    menu.add_item(name, price)
    return jsonify({'message': f'{name} added to menu'})

@app.route('/menu/<name>', methods=['DELETE'])
def remove_menu_item(name):
    menu.remove_item(name)
    return jsonify({'message': f'{name} removed from menu'})

# Routes for Orders
@app.route('/order', methods=['POST'])
def place_order():
    data = request.json
    table_number = data.get('table_number')
    items = data.get('items')
    order = order_manager.place_order(table_number, items)
    return jsonify({'message': f'Order placed for table {table_number}'})

@app.route('/order', methods=['GET'])
def view_orders():
    return jsonify(order_manager.get_orders())

# Routes for Reservation
@app.route('/reserve', methods=['POST'])
def reserve_table():
    data = request.json
    table_number = data.get('table_number')
    if reservation_system.reserve_table(table_number):
        return jsonify({'message': f'Table {table_number} reserved'})
    return jsonify({'message': f'Table {table_number} is already reserved'}), 400

@app.route('/tables', methods=['GET'])
def available_tables():
    return jsonify({'available_tables': reservation_system.get_available_tables()})

# Routes for Billing
@app.route('/bill/<int:table_number>', methods=['GET'])
def generate_bill(table_number):
    order = next((order for order in order_manager.orders if order.table_number == table_number), None)
    if order:
        bill = billing.generate_bill(order)
        return jsonify(bill)
    return jsonify({'message': f'No order found for table {table_number}'}), 404

if __name__ == '__main__':
    app.run(debug=True)
