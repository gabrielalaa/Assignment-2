class Employee(object):
    def __init__(self, employee_id: int, employee_name: str, employee_age: int, salary: float, employee_gender: str):
        self.employee_id: id = employee_id
        self.employee_name: str = employee_name
        self.employee_age: int = employee_age
        self.employee_gender: str = employee_gender
        self.salary: float = salary
