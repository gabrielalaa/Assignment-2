from typing import List
from .order import Order


class Customer(object):
    def __init__(self, customer_id: int, customer_name: str, customer_age: int, customer_gender: str,
                 customer_address: str):
        self.customer_id: int = customer_id
        self.customer_name: str = customer_name
        self.customer_age: int = customer_age
        self.customer_gender: str = customer_gender
        self.customer_address: str = customer_address
        self.order_history: List[Order] = []


# TODO:
#  statistics for age/gender
#  offer recommendations based on the history
#  make it have a valid age? 10 < < 100
