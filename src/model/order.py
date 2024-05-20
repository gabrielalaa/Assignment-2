# TODO list
from typing import List
from .menu import Menu


class Order(object):
    # TODO:
    # F - not delivered; T - delivered or vice versa
    # or make it a string
    def __init__(self, order_id: int, order_status: bool = False):
        self.order_id: int = order_id
        self.order_status: bool = order_status
        self.order_content: List[Menu] = []