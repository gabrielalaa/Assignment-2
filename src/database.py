from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from typing import List

Base = declarative_base()


# Define "Menu_db" using SQLAlchemy's ORM to map it to a database table
class Menu_db(Base):
    __tablename__ = 'products'

    # As a primary key, use the ID
    product_id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    category = Column(String)
    quantity = Column(Integer)
    availability_status = Column(Boolean)


#######################################

# An order can contain multiple menu products
# Construct an association table:
order_menu_association = Table('order_menu', Base.metadata,
                               Column('order_id', Integer, ForeignKey('orders.order_id')),
                               Column('product_id', Integer, ForeignKey('products.product_id')))


# Define "Order_db" using SQLAlchemy's ORM to map it to a database table
class Order_db(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    order_status = Column(String, default='pending')
    # Use a foreign key to link two tables together
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))

    # Create relationships to define hpw different tables are connected
    # back_populates is used to create a bidirectional relationship
    # secondary is used to define a many-to-many relationship
    customer = relationship("Customer_db", back_populates="orders")
    menu_products = relationship("Menu_db", secondary=order_menu_association, back_populates="orders")


#######################################


# Define "Employee_db" using SQLAlchemy's ORM to map it to a database table
class Employee_db(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True)
    employee_name = Column(String)
    employee_age = Column(Integer)


#######################################

# Define "Customer_db" using SQLAlchemy's ORM to map it to a database table
class Customer_db(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    customer_age = Column(Integer)
    customer_gender = Column(String)
    customer_address = Column(String)

    # Relationship
    orders = relationship("Order_db", back_populates="customer")


#######################################

# Set up one engine to my SQLite database
engine = create_engine('sqlite:///McSystem.db', echo=True)
Base.metadata.create_all(engine)

# Set up a session maker to handle transactions
Session = sessionmaker(bind=engine)
# session = Session()


# # Add some entries to the database to check it
# # Create a new menu product
# menu_product = Menu(product_id=1, name="Cheeseburger", price=2.99, category="Burgers", quantity=100, availability_status=True)
#
# # Add the new product to the session
# session.add(menu_product)
#
# # Commit the transaction
# session.commit()
