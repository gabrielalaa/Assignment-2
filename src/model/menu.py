# TODO create the database

class Menu(object):
    # TODO think about how to set the status in the beginning
    def __init__(self, product_id: int, name: str, price: float, category: str, quantity: int, availability_status: bool):
        self.product_id: int = product_id
        self.name: str = name
        self.price: float = price
        self.category: str = category
        self.quantity: int = quantity
        self.availability_status: bool = availability_status
