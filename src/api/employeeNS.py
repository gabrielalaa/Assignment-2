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

# Define the parser for the salary update of an employee
parser = reqparse.RequestParser()
parser.add_argument('salary', type=float, required=True, help='The salary of the employee')

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
    @employee_ns.expect(parser, validate=True)
    @employee_ns.marshal_with(employee_model, envelope='employee')
    def post(self, employee_id):
        arguments = parser.parse_args()
        new_salary = arguments['salary']

        try:
            u_employee = agency.update_employee(employee_id, new_salary)
            return u_employee
        except ValueError as e:
            # Two errors:
            # when we cannot find the employee in the system
            # when the new salary == old salary
            if "employee" in str(e):
                employee_ns.abort(404, str(e))
            else:
                employee_ns.abort(400, str(e))
        except Exception as e:
            employee_ns.abort(500, str(e))

    @employee_ns.doc(description='Delete an employee')
    def delete(self, employee_id):
        try:
            agency.remove_employee(employee_id)
            return jsonify(f'Employee with ID {employee_id} was removed!')
        except Exception as e:
            employee_ns.abort(404, str(e))
