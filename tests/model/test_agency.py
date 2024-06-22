import pytest
from src.model.agency import Agency
from src.model.database import Customer_db, Employee_db


# Tests for customer
# Add customer
def test_add_customer(db_session):
    agency = Agency(session=db_session)
    new_customer_data = {
        "customer_id": 1,
        "customer_name": "Carla Radulescu",
        "customer_age": 20,
        "customer_gender": "female",
        "customer_address": "123 Stone Street",
        "balance": 200
    }

    # Add the customer
    result = agency.add_customer(new_customer_data)
    # Check if the customer was added correctly
    assert result['customer_name'] == 'Carla Radulescu'
    # Check if the customer exists in the database
    assert db_session.query(Customer_db).filter_by(customer_id=1).first() is not None


def test_add_customer_with_the_same_id(db_session):
    agency = Agency(session=db_session)
    new_customer_data = {
        "customer_id": 1,
        "customer_name": "Carla Radulescu",
        "customer_age": 20,
        "customer_gender": "female",
        "customer_address": "123 Stone Street",
        "balance": 200
    }

    # Add the customer
    agency.add_customer(new_customer_data)
    # Should raise an error
    with pytest.raises(ValueError):
        agency.add_customer(new_customer_data)


def test_add_customer_with_wrong_gender(db_session):
    agency = Agency(session=db_session)
    new_customer_data = {
        "customer_id": 1,
        "customer_name": "Carla Radulescu",
        "customer_age": 20,
        "customer_gender": "female",
        "customer_address": "123 Stone Street",
        "balance": 200
    }

    # Add the customer
    agency.add_customer(new_customer_data)
    with pytest.raises(ValueError):
        agency.add_customer(new_customer_data)
    # Should raise an error


# Get customer
def test_get_customer(db_session):
    agency = Agency(session=db_session)
    new_customer_data = {
        "customer_id": 18,
        "customer_name": "Carla Radulescu",
        "customer_age": 20,
        "customer_gender": "female",
        "customer_address": "123 Stone Street",
        "balance": 200
    }
    # Add the customer
    agency.add_customer(new_customer_data)

    # Get the customer
    customer = agency.get_customer(18)
    assert customer['customer_name'] == 'Carla Radulescu'


def test_get_customer_with_wrong_id(db_session):
    agency = Agency(session=db_session)
    with pytest.raises(Exception) as pye:
        agency.get_customer(999)
    assert "does not exist" in str(pye.value)


# Get all customers
def test_all_customers(db_session):
    agency = Agency(session=db_session)
    # Add the first customer
    agency.add_customer({
        "customer_id": 2,
        "customer_name": "Carla Radulescu",
        "customer_age": 20,
        "customer_gender": "female",
        "customer_address": "123 Stone Street",
        "balance": 200
    })
    agency.add_customer({
        "customer_id": 3,
        "customer_name": "Gabriela Radulescu",
        "customer_age": 20,
        "customer_gender": "female",
        "customer_address": "123 Stone Street",
        "balance": 200.60
    })

    customers = agency.all_customers()
    assert len(customers) == 2
    assert customers[0]['customer_name'] == 'Carla Radulescu'
    assert customers[1]['customer_name'] == 'Gabriela Radulescu'


# Remove customer
def test_remove_customer(db_session):
    agency = Agency(session=db_session)
    # Add the customer
    agency.add_customer({
        "customer_id": 181,
        "customer_name": "Carla Radulescu",
        "customer_age": 20,
        "customer_gender": "female",
        "customer_address": "123 Stone Street",
        "balance": 200
    })
    # Remove it
    agency.remove_customer(181)
    # Check if the customer is in the database anymore
    with pytest.raises(Exception) as pye:
        agency.get_customer(181)
    assert "with ID" in str(pye.value)


def test_remove_customer_with_wrong_id(db_session):
    agency = Agency(session=db_session)
    # Try to remove a non-existing customer
    with pytest.raises(Exception) as pye:
        agency.remove_customer(999)
    assert "No customer with ID" in str(pye.value)


# Update customer
def test_update_customer(db_session):
    agency = Agency(session=db_session)
    # Add the customer
    agency.add_customer({
        "customer_id": 181,
        "customer_name": "Carla Radulescu",
        "customer_age": 20,
        "customer_gender": "female",
        "customer_address": "123 Stone Street",
        "balance": 200
    })
    agency.update_customer(181, {'balance': 350.50})
    updated_customer = agency.get_customer(181)
    assert updated_customer['balance'] == 350.50


def test_update_customer_with_wrong_id(db_session):
    agency = Agency(session=db_session)
    with pytest.raises(Exception) as pye:
        agency.update_customer(999, {'balance': 350.50})
    assert "No customer with ID" in str(pye.value)


# Tests for employee
# Add employee
def test_add_employee(db_session):
    agency = Agency(session=db_session)
    new_employee_data = {
        "employee_id": 101,
        "employee_name": "Bob Doe",
        "employee_age": 30,
        "employee_gender": "male",
        "salary": 1200
    }
    # Add the employee
    result = agency.add_employee(new_employee_data)
    # Check if the employee was added correctly
    assert result['employee_name'] == 'Bob Doe'
    # Check if the customer exists in the database
    assert db_session.query(Employee_db).filter_by(employee_id=101).first() is not None


def test_add_employee_with_wrong_id(db_session):
    agency = Agency(session=db_session)
    new_employee_data = {
        "employee_id": 101,
        "employee_name": "Bob Doe",
        "employee_age": 30,
        "employee_gender": "male",
        "salary": 1200
    }

    # Add the employee
    agency.add_employee(new_employee_data)
    # Should raise an error
    with pytest.raises(ValueError):
        agency.add_employee(new_employee_data)


def test_add_employee_with_wrong_gender(db_session):
    agency = Agency(session=db_session)
    new_employee_data = {
        "employee_id": 102,
        "employee_name": "Bob Doe",
        "employee_age": 30,
        "employee_gender": "malee",
        "salary": 1200
    }

    with pytest.raises(ValueError) as pye:
        agency.add_employee(new_employee_data)
    # Should raise an error

    assert "Invalid gender" in str(pye.value)


# Get employee
def test_get_employee(db_session):
    agency = Agency(session=db_session)
    new_employee_data = {
        "employee_id": 103,
        "employee_name": "Bob Doe",
        "employee_age": 30,
        "employee_gender": "male",
        "salary": 1200
    }

    # Add the employee
    agency.add_employee(new_employee_data)

    # Get the employee
    employee = agency.get_employee(103)
    assert employee['employee_name'] == 'Bob Doe'


def test_get_employee_with_wrong_id(db_session):
    agency = Agency(session=db_session)
    with pytest.raises(Exception) as pye:
        agency.get_employee(1111)
    assert "does not exist" in str(pye.value)


# Get all employees
def test_all_employees(db_session):
    agency = Agency(session=db_session)
    # Add the first employee
    agency.add_employee({
        "employee_id": 110,
        "employee_name": "Bob Doe",
        "employee_age": 30,
        "employee_gender": "male",
        "salary": 1200
    })
    # Add the second employee
    agency.add_employee({
        "employee_id": 111,
        "employee_name": "Bob Doe",
        "employee_age": 30,
        "employee_gender": "male",
        "salary": 1200
    })

    employees = agency.all_employees()
    assert len(employees) == 2
    assert employees[0]['employee_name'] == 'Bob Doe'
    assert employees[1]['employee_name'] == 'Bob Doe'


# Remove employee
def test_remove_employee(db_session):
    agency = Agency(session=db_session)
    # Add the customer
    agency.add_employee({
        "employee_id": 115,
        "employee_name": "Bob Doe",
        "employee_age": 30,
        "employee_gender": "male",
        "salary": 1200
    })
    # Remove it
    agency.remove_employee(115)
    # Check if the employee is in the database anymore
    with pytest.raises(Exception) as pye:
        agency.get_employee(115)
    assert "with ID" in str(pye.value)


def test_remove_employee_with_wrong_id(db_session):
    agency = Agency(session=db_session)
    # Try to remove a non-existing employee
    with pytest.raises(Exception) as pye:
        agency.remove_employee(999)
    assert "No employee with ID" in str(pye.value)


# Update employee
def test_update_employee(db_session):
    agency = Agency(session=db_session)
    # Add the employee
    agency.add_employee({
        "employee_id": 120,
        "employee_name": "Bob Doe",
        "employee_age": 30,
        "employee_gender": "male",
        "salary": 1200
    })
    agency.update_employee(120, 2000)
    update_employee = agency.get_employee(120)
    assert update_employee['salary'] == 2000


def test_update_employee_with_wrong_id(db_session):
    agency = Agency(session=db_session)
    with pytest.raises(Exception) as pye:
        agency.update_employee(9999, 1500)
    assert "No employee with ID" in str(pye.value)


