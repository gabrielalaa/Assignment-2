# TODO create the database

class Order(object):
    # TODO:
    # F - not delivered; T - delivered or vice versa
    # or make it a string
    def __init__(self, order_id: int, order_status: bool = False):
        self.order_id = order_id
        self.order_status = order_status
