# Use Flask's request to access submitted data
from flask import request, jsonify
# Import abort to handel errors
from flask_restx import Namespace, fields, Resource, abort, reqparse

# In order to generate my ID's:
import uuid

from ..model.agency import Agency
# Create an instance:
agency = Agency()

customer_ns = Namespace('Customer', description='Customer related operations')

# Define the customer model
customer_model = customer_ns.model('CustomerModel', {
    'customer_id': fields.Integer(required=False,
                                  help='The unique identifier of a customer'),
    'customer_name': fields.String(required=True,
                                   help='The name of the customer'),
    'customer_age': fields.Integer(required=True,
                                   help='The age of the customer'),
    'customer_gender': fields.String(required=True,
                                     help='The gender of the customer',
                                     enum=['female', 'male', 'other', 'unspecified']),
    'customer_address': fields.String(required=True,
                                      help='The address of the customer'),
    'balance': fields.Float(required=True,
                            help='The balance of the customer')
})

# Define the parser for the partial update of a customer
parser = reqparse.RequestParser()
parser.add_argument('customer_name', type=str, required=False, help='The name of the customer')
parser.add_argument('customer_age', type=int, required=False, help='The age of the customer')
parser.add_argument('customer_gender', type=str, required=False, choices=['female', 'male', 'other', 'unspecified'],
                    help='The gender of the customer')
parser.add_argument('customer_address', type=str, required=False, help='The address of the customer')
parser.add_argument('balance', type=float, required=False, help='The balance of the customer')


@customer_ns.route('/')
class CustomerAPI(Resource):
    @customer_ns.doc(description='Add a new customer')
    @customer_ns.expect(customer_model)
    @customer_ns.marshal_with(customer_model, envelope='customer')
    def post(self):
        # Extract the data
        customer_data = customer_ns.payload

        # Create a unique ID
        unique_id = int(str(uuid.uuid4().int)[:8])
        # Customer's IDs will start with 1
        customer_id = int('1' + str(unique_id))

        # Add the ID
        customer_data['customer_id'] = customer_id

        # Try to add a new customer; I want to handle errors here also
        try:
            new_customer = agency.add_customer(customer_data)
            # Return the new customer
            return new_customer
        # Handle the exception if the customer's ID already exist
        except ValueError as e:
            # 400 = Bad request
            customer_ns.abort(400, str(e))
        # Handle other exceptions
        except Exception as e:
            # 500 = Internal Server error
            customer_ns.abort(500, str(e))

    @customer_ns.doc(description='Get all customers')
    @customer_ns.marshal_with(customer_model, envelope='customer')
    def get(self):
        try:
            customers = agency.all_customers()
            return customers
        except Exception as e:
            customer_ns.abort(500, str(e))


@customer_ns.route('/<int:customer_id>')
class CustomerID(Resource):
    @customer_ns.doc(description='Get a specific customer')
    @customer_ns.marshal_with(customer_model, envelope='customer')
    def get(self, customer_id):
        try:
            customer = agency.get_customer(customer_id)
            # If no customer with the given ID is found:
            if not customer:
                customer_ns.abort(404, f'Customer with ID {customer_id} not found!')
            return customer
        except Exception as e:
            customer_ns.abort(500, str(e))

    @customer_ns.doc(description='Delete a customer')
    def delete(self, customer_id):
        try:
            # customer = agency.get_customer(customer_id)
            # # If no customer with the given ID is found:
            agency.remove_customer(customer_id)
            return jsonify(f'Customer with ID {customer_id} was removed!')
        except ValueError as e:
            customer_ns.abort(404, str(e))
        except Exception as e:
            customer_ns.abort(500, str(e))
