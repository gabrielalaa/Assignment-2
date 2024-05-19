# TODO create the database

class Employee(object):
    # TODO think about adding salary, gender, age, position etc.
    def __init__(self, employee_id: int, employee_name: str, employee_age: int):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_age = employee_age
        # self.salary = 0
