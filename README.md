# Assignment 2 - McDonald's System
## Deadline: 23.06.2024, 23:00

---

### Introduction
#### Welcome to the McDonald's System Project
This project is about building a system for McDonald's that helps employees and customers interact more effectively.
Employees can change the menu as needed, and customers can place their orders through a simple interface.

### What does the system do?
* Add, get, update and remove employees which are stored in a database.
* Add, get, update, and remove customers which are stored in a database.

### Behind the Scenes
* I used an existing layout like we did for the previous project
* I set up an API that lets the front-end of the application communicate with the database
* I tested the system (the agency which contains my methods) using `pytest` to make sure everything works as I expected

Such a system can be beneficial for both the staff and the customers. They can make things faster using an interface which is easy to use.

---

## Functionality
The API consists of the following main functionality

**Management of customers**
* Add/get/update/remove a customer. Each customer has a (unique) ID which starts with '1', a name, an age, a gender, an address and a balance.
* Valid genders are: female, male, other and unspecified.
* Partial updates can be done: customer_address and balance.

**Management of employees**
* Add/get/update/remove an employee. Each employee has a (unique) ID which starts with '2', a name, an age a gender and a salary.
* Valid genders are: female, male, other and unspecified.
* Updates can be made over salary only.

**Management of database**
* I used SQLAlchemy because I found it much easier to implement because it is using classes and objects.
* I created a `database` python file in `src.model` in which I defined Menu_db, Order_db, Customer_db and Employee_db; I set up the engine and a session maker to handle transactions. 
* The database is created in my root of the project. I won't import it. It will be created automatically when using the application on the browser.

**Testing**
* I created tests using `pytest` for my `agency` file which is found in `src.model`
* I used an in-memory database because I didn't want to affect the actual database of my project.

**Important note**
To make unique ID's I used the uuid module. 
I preferred to make it shorter only of 8 digits, adding a (different) prefix for each. 

---

## API Endpoints

| Endpoint                | HTTP Method | Description        |
|-------------------------|-------------|--------------------|
| /customer               | post        | Add a new customer |
| /customer               | get         | Get all customers  |
| /customer/{customer_id} | get         | Get a customer     | 
| /customer/{customer_id} | post        | Update a customer  | 
| /customer/{customer_id} | delete      | Delete a customer  | 
| /employee               | post        | Add a new employee |
| /employee               | get         | Get all employee   |
| /employee/{employee_id} | get         | Get a employee     | 
| /employee/{employee_id} | post        | Update a employee  | 
| /employee/{employee_id} | delete      | Delete a employee  | 

---

## Technical aspects

### Python Version
At the beginning I was using 3.9. At the very end, I changed to 3.10.

### Packages and their versions
Using the command `pip list`:
* aniso8601                 9.0.1 
* attrs                     23.2.0 
* blinker                   1.8.2 
* click                     8.1.7 
* colorama                  0.4.6 
* exceptiongroup            1.2.1 
* Flask                     3.0.3 
* flask-restx               1.3.0 
* greenlet                  3.0.3 
* importlib_resources       6.4.0 
* iniconfig                 2.0.0 
* itsdangerous              2.2.0 
* Jinja2                    3.1.4 
* jsonschema                4.22.0 
* jsonschema-specifications 2023.12.1 
* MarkupSafe                2.1.5 
* packaging                 24.1 
* pip                       23.2.1 
* pluggy                    1.5.0 
* rpds-py                   0.18.1 
* setuptools                68.2.0 
* SQLAlchemy                2.0.31 
* tomli                     2.0.1 
* typing_extensions         4.12.2 
* Werkzeug                  3.0.3 
* wheel                     0.41.2

**Important Note**
Some of them are included in the `requirements` txt file.
