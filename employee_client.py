# This is the client for the employee
import socket
import json


def send_request(action, data=None):
    # Send a request to the server and return the response as a dictionary
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9001))

    # Take the initial connection response
    initial_response = client.recv(1024).decode('utf-8')
    try:
        initial_response = json.loads(initial_response)
        print(f'The initial response from the server: {initial_response}')
    except json.JSONDecodeError:
        print(f'The initial response is not in json: {initial_response}')

    request = json.dumps({'action': action, **(data if data else {})})
    client.sendall(request.encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    print(f'Response from server: {response}')
    client.close()
    return json.loads(response)


def get_menu():
    # Get the menu from the server
    response = send_request('get_menu')
    if response['status'] == 'success':
        print("Menu:")
        for index, item in enumerate(response['menu_list'], start=1):
            print(f'{index}. {item["name"]} - Price: {item["price"]} $ - Category: {item["category"]} - Quantity: {item["quantity"]}')
    else:
        print("Error:", response['message'])


def update_menu(product_id, name, price, category, quantity):
    # Update a product
    data = {'product_id': product_id, 'name': name, 'price': price, 'category': category, 'quantity': quantity}
    response = send_request('update_menu', data)
    if response['status'] == 'success':
        print(response['message'])
    else:
        print("Error:", response['message'])


def add_product(name, price, category, quantity):
    # Add a new product
    data = {'name': name, 'price': price, 'category': category, 'quantity': quantity}
    response = send_request('add_product', data)
    if response['status'] == 'success':
        print(response['message'])
    else:
        print("Error:", response['message'])


def delete_product(product_id):
    # Delete a product
    data = {'product_id': product_id}
    response = send_request('delete_product', data)
    if response['status'] == 'success':
        print(response['message'])
    else:
        print("Error:", response['message'])


if __name__ == '__main__':
    while True:
        print("\nEmployee Menu:")
        print("1. View Menu")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Enter your choice: 1, 2, 3, 4 or 5 ")
        if choice == '1':
            get_menu()
        elif choice == '2':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            category = input("Enter product category: Burgers, Fries, Salads, Drinks, Desserts ")
            quantity = int(input("Enter product quantity: "))
            add_product(name, price, category, quantity)
        elif choice == '3':
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new product name: ")
            price = float(input("Enter new product price: "))
            category = input("Enter new product category : Burgers, Fries, Salads, Drinks, Desserts ")
            quantity = int(input("Enter new product quantity: "))
            update_menu(product_id, name, price, category, quantity)
        elif choice == '4':
            product_id = int(input("Enter product ID to delete: "))
            delete_product(product_id)
        elif choice == '5':
            break
        else:
            print("Invalid request. Please try again!")
