from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# Define "Menu" using SQLAlchemy's ORM to map it to a database table
class Menu(Base):
    __tablename__ = 'products'

    # As a primary key, use the ID
    product_id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    category = Column(String)
    quantity = Column(Integer)
    availability_status = Column(Boolean)


# Set up the engine to my SQLite database
engine = create_engine('sqlite:///menu.db', echo=True)
Base.metadata.create_all(engine)

# Set up a session maker to handle transactions
Session = sessionmaker(bind=engine)
session = Session()

# # Add some entries to the database to check it
# # Create a new menu product
# menu_product = Menu(product_id=1, name="Cheeseburger", price=2.99, category="Burgers", quantity=100, availability_status=True)
#
# # Add the new product to the session
# session.add(menu_product)
#
# # Commit the transaction
# session.commit()

