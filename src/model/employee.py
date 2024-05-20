class Employee(object):
    def __init__(self, employee_id: int, employee_name: str, employee_age: int, salary: float, employee_gender: str):
        self.employee_id: id = employee_id
        self.employee_name: str = employee_name
        self.employee_age: int = employee_age
        self.employee_gender: str = employee_gender
        self.salary: float = salary

# TODO:
#  to work you should have the age of 16+ <= 50
#  salary > 0
#  add, remove, update employees from the system
#  maybe make a statistics based on age/gender/salary
#  or some additional things about the salary
