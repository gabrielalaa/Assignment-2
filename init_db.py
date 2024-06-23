from sqlalchemy import create_engine
from src.model.database import Base, Menu_db
from sqlalchemy.orm import sessionmaker


def initialize_database():
    # Set up one engine to my SQLite database
    engine = create_engine('sqlite:///McSystem.db', echo=True)
    Base.metadata.create_all(engine)
    # print(Base.metadata.tables)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Add elements in menu
    menu_items = [
        Menu_db(name="Big Mac", price=5.99, category="Burgers", quantity=50),
        Menu_db(name="French Fries", price=3, category="Fries", quantity=100),
        Menu_db(name="Chicken Salad", price=5, category="Salads", quantity=40),
        Menu_db(name="Coca Cola", price=2, category="Drinks", quantity=150),
        Menu_db(name="Baked Apple Pie", price=2.49, category="Desserts", quantity=30)
    ]

    session.add_all(menu_items)
    session.commit()


if __name__ == '__main__':
    initialize_database()
