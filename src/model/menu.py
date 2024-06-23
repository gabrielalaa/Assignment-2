class Menu(object):
    def __init__(self, product_id: int, name: str, price: float, category: str, quantity: int):
        self.product_id: int = product_id
        self.name: str = name
        self.price: float = price
        self.category: str = category
        self.quantity: int = quantity

