from .database import Session, Customer_db


# Menu_db, Order_db , Employee_db


# Create a class to import all the methods easily
class Agency:
    def __init__(self):
        # Use the session to commit and access data
        # Create a new session instance:
        self.session = Session()

    # First of all, I need to have customers and employees in my system
    # METHODS for customer
    def add_customer(self, customer_data):
        # Include error handling
        try:
            # Assert that ID does not exist using filter_by().first()
            # which returns the first matched instance without loading other data
            existing_customer = self.session.query(Customer_db).filter_by(
                customer_id=customer_data['customer_id']).first()
            if existing_customer:
                raise ValueError(f"A customer with ID {customer_data['customer_id']} already exists!")

            # Create the new_customer, extracting his/her data
            new_customer = Customer_db(**customer_data)
            # Add the new_customer to the database
            self.session.add(new_customer)
            # Commit the changes
            self.session.commit()
            # Convert SQLAlchemy object to a dictionary
            return {obj.name: getattr(new_customer, obj.name) for obj in new_customer.__table__.columns}
        except Exception as e:
            # If any operation fails, use "rollback()" to ensure that none of the changes take effect
            self.session.rollback()
            raise ValueError(f"An error occurred while adding the customer: {str(e)}")
        finally:
            # In any situation, make sure to close the session:
            self.session.close()

    def get_customer(self, customer_id):
        try:
            # Find the first customer with the given ID
            customer = self.session.query(Customer_db).filter(Customer_db.customer_id == customer_id).first()
            if customer is None:
                return None
            return {obj.name: getattr(customer, obj.name) for obj in customer.__table__.columns}
        except Exception as e:
            raise Exception(f"An error occurred while getting the customer: {str(e)}")
        finally:
            # Make sure to close the session:
            self.session.close()

    def all_customers(self):
        try:
            customers = self.session.query(Customer_db).all()
            return [{obj.name: getattr(customer, obj.name) for obj in Customer_db.__table__.columns}
                    for customer in customers]
        except Exception as e:
            raise Exception(f"An error occurred while getting all the customers: {str(e)}")
        finally:
            # Make sure to close the session:
            self.session.close()

    def remove_customer(self, customer_id):
        try:
            # Find the customer with the given ID
            r_customer = self.session.query(Customer_db).filter_by(customer_id=customer_id).first()
            if not r_customer:
                raise ValueError(f"No customer with ID {customer_id}")

            # If customer exists, remove it
            self.session.delete(r_customer)
            self.session.commit()
            # Return it for confirmation
            return {obj.name: getattr(r_customer, obj.name) for obj in r_customer.__table__.columns}
        except Exception as e:
            raise Exception(f"An error occurred while removing the customer : {str(e)}")
        finally:
            # Make sure to close the session:
            self.session.close()

    # TODO: update_customer
