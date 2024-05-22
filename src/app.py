from flask import Flask
from flask_restx import Api


# from .api.menuNS import menu_ns
# from .api.orderNS import order_ns
# from .api.customerNS import customer_ns
# from .api.employeeNS import employee_ns

# from .model.agency import Agency

# agency = Agency()


def create_app():
    paperroute_app = Flask(__name__)
    # need to extend this class for custom objects, so that they can be jsonified
    paperroute_api = Api(paperroute_app, title="McDonalds: An app for both customers and employees")

    # add individual namespaces
    # paperroute_api.add_namespace(menu_ns)
    # paperroute_api.add_namespace(order_ns)
    # paperroute_api.add_namespace(customer_ns)
    # paperroute_api.add_namespace(employee_ns)

    return paperroute_app


if __name__ == '__main__':
    create_app().run(debug=False, port=80)
