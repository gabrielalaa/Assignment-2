# This is the client for the customer
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
        print("Menu:", response['menu_list'])
    else:
        print("Error:", response['message'])


def place_order(customer_id, order):
    # Place an order
    data = {'customer_id': customer_id, 'order': order}
    response = send_request('place_order', data)
    if response['status'] == 'success':
        print(response['message'])
    else:
        print("Error:", response['message'])


if __name__ == '__main__':
    customer_id = int(input('Enter your customer ID: '))

    while True:
        print("\nCustomer Menu: ")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Exit")

        choice = input('Enter your choice: 1, 2 or 3 ')
        if choice == '1':
            get_menu()
        elif choice == '2':
            order = []
            while True:
                product_id = int(input('Enter product ID: '))
                quantity = int(input('Enter quantity: '))
                order.append({'product_id': product_id, 'quantity': quantity})
                more = input('Do you want more products? (yes/no): ')
                if more.lower() != 'yes':
                    break
            place_order(customer_id, order)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again!")
