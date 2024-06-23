# Manage the server side of a TCP socket
import socket
import threading
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.model.database import Menu_db, Customer_db, Order_db

engine = create_engine('sqlite:///McSystem.db', echo=True)
Session = sessionmaker(bind=engine)


def client(client_socket):
    # Handle clients requests
    try:
        # Log in on the server side:
        print(f'Client connected.')
        # Send this message to the client:
        client_socket.sendall(json.dumps({'status': 'connected', 'message': 'Welcome to the server!'}).encode('utf-8'))
        while True:
            # Get the request from the client
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                break

            print(f'Received: {request}')
            response = process_request(request)
            client_socket.sendall(response.encode('utf-8'))
            print(f'Response: {response}')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        print(f'Client disconnected.')
        client_socket.close()


def process_request(request):
    # Find what kind of request the client asked for and return an appropriate response
    try:
        data = json.loads(request)
        action = data.get('action')
        if action == 'get_menu':
            return get_menu()
        elif action == 'update_menu':
            return update_menu(data)
        elif action == 'delete_product':
            return delete_product(data)
        elif action == 'add_product':
            return add_product(data)
        elif action == 'place_order':
            return place_order(data)
        else:
            return json.dumps({'status': 'error', 'message': 'Invalid action! Please try: get_menu, update_menu, '
                                                             'delete_product, add_product or place_order'})
    except Exception as e:
        return json.dumps({'status': 'error', 'message': str(e)})


def get_menu():
    # Get the menu from the database
    session = Session()
    menu_products = session.query(Menu_db).all()
    menu_list = [{'product_id': item.product_id, 'name': item.name, 'price': item.price, 'category': item.category, 'quantity': item.quantity} for item in menu_products]
    session.close()
    return json.dumps({'status': 'success', 'menu_list': menu_list})


def update_menu(data):
    # Update the products from the menu
    session = Session()
    try:
        menu_item = session.query(Menu_db).get(data['product_id'])
        if menu_item:
            menu_item.name = data['name']
            menu_item.price = data['price']
            menu_item.category = data['category']
            menu_item.quantity = data['quantity']
            session.commit()
            return json.dumps({'status': 'success', 'message': 'Product updated successfully'})
        else:
            return json.dumps({'status': 'error', 'message': 'Product not found'})
    except Exception as e:
        # In case of any error, rollback
        session.rollback()
        return json.dumps({'status': 'error', 'message': str(e)})
    finally:
        # Make sure to close the session
        session.close()


def delete_product(data):
    # Delete a product from the database
    session = Session()
    try:
        product = session.query(Menu_db).get(data['product_id'])
        if product:
            session.delete(product)
            session.commit()
            return json.dumps({'status': 'success', 'message': 'Product deleted successfully'})
        else:
            return json.dumps({'status': 'error', 'message': 'Product not found'})
    except Exception as e:
        session.rollback()
        return json.dumps({'status': 'error', 'message': str(e)})
    finally:
        session.close()


def add_product(data):
    # Add a new product in the database
    session = Session()
    try:
        new_product = Menu_db(
            name=data['name'],
            price=data['price'],
            category=data['category'],
            quantity=data['quantity']
        )
        session.add(new_product)
        session.commit()
        return json.dumps({'status': 'success', 'message': 'Product added successfully'})
    except Exception as e:
        session.rollback()
        return json.dumps({'status': 'error', 'message': str(e)})
    finally:
        session.close()


def place_order(data):
    # Order food as a customer
    session = Session()
    try:
        # Get the customer first
        customer = session.query(Customer_db).get(data['customer_id'])
        # If the customer exists
        if customer:
            # Initialize the total cost of the order
            total_cost = 0
            for item in data['order']:
                # If the item exists in the menu, get it
                product = session.query(Menu_db).get(item['product_id'])
                # Check the quantity
                if product and product.quantity >= item['quantity']:
                    # Calculate the total cost
                    total_cost += product.price * item['quantity']
                    product.quantity -= item['quantity']
                else:
                    return json.dumps({'status': 'error', 'message': 'Product not available or insufficient quantity, '
                                                                     'we are sorry!'})

            # Check the customer balance - a customer cannot place orders without having money
            if customer.balance >= total_cost:
                customer.balance -= total_cost
                # Update the status of the order
                order = Order_db(customer_id=customer.customer_id, order_status='preparing')
                session.add(order)
                session.commit()
                response = json.dumps({'status': 'success', 'message': 'Order is being prepared!'})

                # Simulate order preparation
                import time
                time.sleep(5)
                order.order_status = 'completed'
                session.commit()

                for item in data['order']:
                    menu_item = session.query(Menu_db).get(item['product_id'])
                    order.menu_products.append(menu_item)
                session.add(order)
                session.commit()
                return json.dumps({'status': 'success', 'message': 'Order delivered successfully. Enjoy your meal!'})
            else:
                return json.dumps({'status': 'error', 'message': 'Not enough money'})
        else:
            return json.dumps({'status': 'error', 'message': 'Customer not found'})
    except Exception as e:
        session.rollback()
        return json.dumps({'status': 'error', 'message': str(e)})
    finally:
        session.close()


def start_server():
    # Start the TCP server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9001))
    server.listen(5)
    print('Server listening on port 9001')

    while True:
        conn, addr = server.accept()
        print('Connected by', addr)
        client_handle = threading.Thread(target=client, args=(conn,))
        client_handle.start()


if __name__ == '__main__':
    start_server()
