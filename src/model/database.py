from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine, Table, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# Define "Menu_db" using SQLAlchemy's ORM to map it to a database table
class Menu_db(Base):
    __tablename__ = 'products'

    # As a primary key, use the ID
    product_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    # I want to fix some simple categories to make the navigation as a user much easier and logical
    category = Column(Enum("Burgers", "Fries", "Salads", "Drinks", "Desserts", name="menu_categories"), nullable=False)
    quantity = Column(Integer, nullable=False)


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

    # Create relationships to define how different tables are connected
    # back_populates is used to create a bidirectional relationship
    # secondary is used to define a many-to-many relationship
    customer = relationship("Customer_db", back_populates="orders")
    menu_products = relationship("Menu_db", secondary=order_menu_association, back_populates="orders")


#######################################

# Define "Employee_db" using SQLAlchemy's ORM to map it to a database table
class Employee_db(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True)
    employee_name = Column(String, nullable=False)
    employee_age = Column(Integer, nullable=False)
    employee_gender = Column(Enum('female', 'male', 'other', 'unspecified', name='gender_types'), nullable=False)
    salary = Column(Float, nullable=False)

#######################################


# Define "Customer_db" using SQLAlchemy's ORM to map it to a database table
class Customer_db(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)
    customer_age = Column(Integer, nullable=False)
    customer_gender = Column(Enum('female', 'male', 'other', 'unspecified', name='gender_types'), nullable=False)
    customer_address = Column(String, nullable=False)
    balance = Column(Float, nullable=False)

    # Relationship
    orders = relationship("Order_db", back_populates="customer")


Menu_db.orders = relationship("Order_db", secondary=order_menu_association, back_populates="menu_products")

#######################################

# Set the engine and sessionmaker accessible
engine = create_engine('sqlite:///McSystem.db', echo=True)

# Set up a session maker to handle transactions
Session = sessionmaker(bind=engine)
