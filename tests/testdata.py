from ..src.model.database import Customer_db, Employee_db


def create_customers(session):
    # Create customer instances
    customers = [
        Customer_db(customer_id=1, customer_name="Gabriela", customer_age=20, customer_gender='female',
                    customer_address='123 Main Street', balance=100),
        Customer_db(customer_id=2, customer_name="Alex", customer_age=25, customer_gender='male',
                    customer_address='456 Main Street', balance=150.75)
    ]
    session.add(customers)
    session.commit()


def create_employees(session):
    # Create employee instances
    employees = [
        Employee_db(employee_id=3, employee_name="Alice", employee_age=28, employee_gender='female', salary=1000),
        Employee_db(employee_id=4, employee_name="Bob", employee_age=35, employee_gender='male', salary=1500)
    ]
    session.add(employees)
    session.commit()


# Populate the database before tests are run
def populate(session):
    create_customers(session)
    create_employees(session)

