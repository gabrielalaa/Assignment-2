# Use Flask's request to access submitted data
from flask import request, jsonify
# Import abort to handel errors
from flask_restx import Namespace, fields, Resource, abort, reqparse

# In order to generate my ID's:
import uuid

from ..model.agency import Agency

# Create an instance:
agency = Agency()

employee_ns = Namespace('Employee', description='Employee related operations')
# Define the employee model
employee_model = employee_ns.model('EmployeeModel', {
    'employee_id': fields.Integer(required=False,
                                  help='The unique identifier of an employee'),
    'employee_name': fields.String(required=True,
                                   help='The name of the employee'),
    'employee_age': fields.Integer(required=True,
                                   help='The age of the employee'),
    'employee_gender': fields.String(required=True,
                                     help='The gender of the employee',
                                     enum=['female', 'male', 'other', 'unspecified']),
    'salary': fields.Float(required=True,
                           help='The salary of the employee')
})

# # Define the parser for the partial update of an employee
# parser = reqparse.RequestParser()

# # parser.add_argument('customer_name', type=str, required=False, help='The name of the customer')
# # parser.add_argument('customer_age', type=int, required=False, help='The age of the customer')
# # parser.add_argument('customer_gender', type=str, required=False, choices=['female', 'male', 'other', 'unspecified'],
# #                     help='The gender of the customer')
# parser.add_argument('customer_address', type=str, required=False, help='The address of the customer')
# parser.add_argument('balance', type=float, required=False, help='The balance of the customer')


@employee_ns.route('/')
class EmployeeAPI(Resource):
    @employee_ns.doc(description='Add a new employee')
    @employee_ns.expect(employee_model)
    @employee_ns.marshal_with(employee_model, envelope='employee')
    def post(self):
        # Extract the data
        employee_data = employee_ns.payload

        # Create a unique ID
        unique_id = int(str(uuid.uuid4().int)[:8])
        # Employee's IDs will start with 2
        employee_id = int('2' + str(unique_id))

        # Add the ID
        employee_data['employee_id'] = employee_id

        # Try to add a new employee
        try:
            new_employee = agency.add_employee(employee_data)
            # Return the new employee
            return new_employee
        # Handle the exception if the employee's ID already exist
        except ValueError as e:
            # 400 = Bad request
            employee_ns.abort(400, str(e))
        # Handle other exceptions
        except Exception as e:
            # 500 = Internal Server error
            employee_ns.abort(500, str(e))

    @employee_ns.doc(description='Get all employees')
    @employee_ns.marshal_with(employee_model, envelope='employee')
    def get(self):
        try:
            employees = agency.all_employees()
            return employees
        except Exception as e:
            employee_ns.abort(500, str(e))


@employee_ns.route('/<int:employee_id>')
class EmployeeID(Resource):
    @employee_ns.doc(description='Get a specific employee')
    @employee_ns.marshal_with(employee_model, envelope='employee')
    def get(self, employee_id):
        try:
            employee = agency.get_employee(employee_id)
            return employee
        except Exception as e:
            employee_ns.abort(404, str(e))

    @employee_ns.doc('Update an employee')
    # @employee_ns.expect(parser, validate=True)
    @employee_ns.marshal_with(employee_model, envelope='employee')
    def post(self, employee_id):
        # arguments = parser.parse_args()
        # Take only the new values from the arguments that are not None
        # new_data = {key: value for key, value in arguments.items() if value is not None}

        # Check if the employee exists
        check_employee = agency.get_employee(employee_id)
        if not check_employee:
            employee_ns.abort(404, f'No employee with ID {employee_id} found!')

        # # Check if there are any updates
        # if not new_data:
        #     employee_ns.abort(400, 'No updates')

#         # Check if there are any updates
#         if not new_data:
#             customer_ns.abort(400, 'No updates')
#
#         try:
#             u_customer = agency.update_customer(customer_id, new_data)
#             if not u_customer:
#                 customer_ns.abort(400, "No updates")
#             return u_customer
#         except ValueError as e:
#             customer_ns.abort(404, str(e))
#         except Exception as e:
#             customer_ns.abort(500, str(e))

    @employee_ns.doc(description='Delete an employee')
    def delete(self, employee_id):
        try:
            employee = agency.get_employee(employee_id)
            agency.remove_employee(employee_id)
            return jsonify(f'Employee with ID {employee_id} was removed!')
        except Exception as e:
            employee_ns.abort(404, str(e))
