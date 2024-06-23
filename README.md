# Assignment 2 - McDonald's System
## Deadline: 23.06.2024, 23:00

---

## Introduction
### Welcome to the McDonald's System Project
This project is about building a system for McDonald's that helps employees and customers interact more effectively.
Employees can change the menu as needed, and customers can place their orders through a simple interface.

### What does the system do?
* Add, get, update and remove employees which are stored in a database.
* Add, get, update, and remove customers which are stored in a database.

### Behind the Scenes
* I used an existing layout like we did for the previous project
* I set up an API that lets the front-end of the application communicate with the database
* I tested the system (the agency which contains my methods) using `pytest` to make sure some of the things work as I expected
* I created a connection between clients and menu using a basic socket. They can place orders. After each order, all the changes will appear in databases.
* I created a simple connection between employees and menu. They can perform actions over the menu (add/update/remove products).

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
* I used SQLAlchemy. I found it much easier to implement because it is using classes and objects.
* I wanted to have some items in my `Menu_db` database, therefore I created another file called `init_db.py`. This initializes the database and adds elements in the menu. **This should be the first to be run, once!**
* I created a `database.py` in `src.model` in which I defined Menu_db, Order_db, Customer_db and Employee_db. 
* I set up the engine and a session maker to handle transaction.
* The database is created in my root of the project. I won't import it. It will be created automatically after running `init_db.py`. Customers and employees databases will be modified when using the application on the browser. Menu and order databases are modified after communicating with the server.

**Testing**
* I created tests using `pytest` for my `agency.py` file which is found in `src.model`
* I used an in-memory database because I didn't want to affect the actual database of my project.
* I was not able to create tests for `customerNS` and `employeeNS`. I couldn't figure it out why my database was affected even if I specified an in-memory one. In addition, some tests were failing even if there have been noticeable changes in my database. A similar thing happened with testing my server and my client.
* I have only 20 tests.

**Networking**
* Unfortunately, it is visible just in python. I tried to keep it in `src` in a folder I created called `network`. But I had several errors in which the menu database seemed not to exist, that it could not be accessed.
* It can be found in the root of the project. 
* There is one server called `server.py` 
* One client for employees called `employee_client.py`
* Another client for customers called `customer_client.py`
* Both can communicate with the server at the same time.
* TIP1: If you want to see the database (if it is not visible in `McSystem.db`) go to `verify.py` file and this will return what `Menu_db` contains.
* TIP2: Pay attention to the values that already exist in the database. In order to interact with the server as a customer you must mention a valid ID. Moreover, as an employee, if you want to remove a product (using its ID), while communicating with the server, the ID will not be provided. SQLAlchemy assigns IDs for the elements that are directly created in `init_db` in increasing order starting from 1. And when viewing the menu, I used enumerate which also starts from 1. **ID != INDEX**

**Important note**
* To make unique ID's I used the uuid module. I preferred to make it shorter only of 8 digits, adding a (different) prefix for each. 
* The part related to networking was the hardest. I haven't been able to do it the way I wanted: to be able to see it when you start the app and interact right there. I tried socketio but it was difficult. And using a simple TCP socket was going too complex.

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
Some of them are included in the `requirements.txt` file.

---

## How to use the project ?
* Clone it into your device.
* Set up your environment (python version 3.9 or 3.10) and download the packages that I have specified in `requirements.txt`. 
* First, run `init_db.py` once to initialize the database. From my experience, I was not able to see that `Menu_db` was successfully created, so I wrote a short code in `verify.py` to check if everything works well.
* Then, navigate to `start.py` and run it. The application will be available on the browser. There you can handle customers and employees actions (add/get/update/remove).
* If you want to communicate with the server to access the menu as an employee, go in the root of the project and run `server.py` and `employee_client.py`. Instructions will be provided there. Same for `customer_client.py`.
* If you want to check my project, I have created some tests in `tests` folder. Just type in `pytest` in the terminal.

---

## Conclusion 

I enjoyed doing this project. I am satisfied with the result I have. And I am sure that if I had focused more, I could have achieved everything I set out to do. 
It was much more complex than I originally imagined. And I think using something else like django, it would have been much easier and faster to do.

__Project by Radulescu Carla Gabriela, group 2.__
