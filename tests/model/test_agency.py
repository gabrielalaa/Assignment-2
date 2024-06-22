import pytest
from ...src.model.agency import Agency
from ...src.model.database import Customer_db, Employee_db


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

