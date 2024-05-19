# MODEL 1
# # complete it !
#
# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
#
# engine = create_engine('sqlite://mydb1.db', echo=True)
#
# meta = MetaData()
#
# employees = Table(
#     'employees', meta,
#     Column('id', Integer, primary_key=True), Column('name', String),
#     Column('salary', Float), Column('position', String), Column('hiredate', String),
# )
#
# insert_statement = employees.insert().values(name='John', salary='12939')
#
# connection = engine.connect()
#
# connection.execute(insert_statement)
#
#
# s = employees.select()
# result = connection.execute(s)
#
# for row in result:
#     print(row)
#
# meta.create_all(engine)


# MODEL 2
# from sqlalchemy import Column, Integer, String, Float, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# Base = declarative_base()
#
#
# class Employee(Base):
#     __tablename__ = 'employees'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     salary = Column(Float)
#     email = Column(String)
#
#     def __init__(self):
#         pass
#
#
# engine = create_engine('sqlite:///mybd2.db', echo=True)
#
# Base.metadata.create_all(engine)
#
# SessionClass = sessionmaker(bind=engine)
# session = SessionClass()
#
# e1 = Employee()
# e2 = Employee()
#
# e1.email = 'happy@gmail.com'
# e2.email = 'sad@gmail.com'
#
# session.add(e1)
# session.add(e2)
#
# session.commit()