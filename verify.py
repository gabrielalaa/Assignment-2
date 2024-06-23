# This file was created to verify if the database was created successfully

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.model.database import Menu_db

engine = create_engine('sqlite:///McSystem.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def verify_database():
    menu_items = session.query(Menu_db).all()
    for item in menu_items:
        print(f"ID: {item.product_id}, Name: {item.name}, Price: {item.price}, Category: {item.category}, Quantity: {item.quantity}")


if __name__ == '__main__':
    verify_database()
    session.close()
