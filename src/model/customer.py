# TODO create the database

class Customer(object):
    # TODO think of adding/removing things
    def __init__(self, customer_id: int, customer_name: str, age:int, gender: str, customer_address: str, order_history: list):
        self.customer_id = customer_id
        self.customer_name: str = customer_name
        self.age: int = age
        self.gender: str = gender
        self.customer_address: str = customer_address
        self.order_history: list = order_history
