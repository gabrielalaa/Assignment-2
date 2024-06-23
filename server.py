# Manage the server side of a TCP socket
import socket
import threading
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.model.database import Menu_db

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
        else:
            return json.dumps({'status': 'error', 'message': 'Invalid action! Please try: get_menu, update_menu, '
                                                             'delete_product or add_product'})
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


def start_server():
    # Start the TCP server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9000))
    server.listen(5)
    print('Server listening on port 9000')

    while True:
        conn, addr = server.accept()
        print('Connected by', addr)
        client_handle = threading.Thread(target=client, args=(conn,))
        client_handle.start()


if __name__ == '__main__':
    start_server()
