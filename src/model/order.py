from typing import List
from .menu import Menu


class Order(object):
    def __init__(self, order_id: int, order_status: str = "pending", customer_id: int = None):
        self.order_id: int = order_id
        self.order_status: str = order_status
        self.order_content: List[Menu] = []
        self.customer_id: int = customer_id

    def set_customer(self, customer_id: int):
        self.customer_id = customer_id

# TODO: make the order as a customer (add items to order, remove items from order)
#  update the status

# TODO:
#  an order cannot be made without any product in order_content
