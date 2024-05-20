# TODO list
from typing import List
from .order import Order


class Customer(object):
    # TODO think of adding/removing attributes
    def __init__(self, customer_id: int, customer_name: str, age:int, gender: str, customer_address: str):
        self.customer_id: int = customer_id
        self.customer_name: str = customer_name
        self.age: int = age
        self.gender: str = gender
        self.customer_address: str = customer_address
        self.order_history: List[Order] = []
