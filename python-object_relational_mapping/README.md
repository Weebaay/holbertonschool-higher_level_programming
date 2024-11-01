# Python - Object-Relational Mapping (ORM) Project

This project combines two essential components of backend development: databases and Python! You will explore SQL and ORM techniques, learning how to connect Python to MySQL databases and how to use SQLAlchemy to simplify database interactions.

## Project Overview

In this project:
1. **Using MySQLdb**: You will connect Python scripts to a MySQL database to query and modify data using SQL.
2. **Using SQLAlchemy (ORM)**: SQLAlchemy helps map Python objects to database tables, enabling you to perform database operations with Python code rather than SQL statements.

This structure allows your code to be database-agnostic, meaning you can switch database providers without changing the code’s core logic.

---

## Learning Objectives

By the end of this project, you should understand:
- How to connect to a MySQL database from a Python script.
- How to execute SQL commands (SELECT, INSERT, etc.) from Python.
- The concept of Object-Relational Mapping (ORM).
- Mapping Python classes to MySQL tables using SQLAlchemy.

## Requirements

- **Languages**: Python 3.8.5
- **Database**: MySQL 8.0
- **Libraries**:
  - `MySQLdb` (MySQL client for Python)
  - `SQLAlchemy` (Object-relational mapper)

## Project Setup

### Installing MySQL 8.0

```bash
sudo apt update
sudo apt install mysql-server
mysql --version
```
**To start MySQL, run:**
	sudo mysql
### Installing MySQLdb

**Make sure MySQL is installed first.**
	sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
	sudo pip3 install mysqlclient

### Installing SQLAlchemy
	sudo pip3 install SQLAlchemy

## Tasks

| Task Number | Task | Description |
| ----------- | ---- | ----------- |
| **0**       | **Get all states** | List all states from the database `hbtn_0e_0_usa`. |
| **1**       | **Filter states** | List all states with names starting with "N". |
| **2**       | **Filter states by user input** | List all states matching a user-provided name. |
| **3**       | **SQL Injection Protection** | List states by name input without allowing SQL injection. |
| **4**       | **Cities by states** | List all cities with their respective states. |
| **5**       | **All cities by state** | List all cities of a specific state, provided by the user. |
| **6**       | **First state model** | Define a Python class `State` mapped to the `states` table. |
| **7**       | **All states via SQLAlchemy** | List all State objects from the database using SQLAlchemy. |
| **8**       | **First state** | Print the first state object from the database. |
| **9**       | **Contains `a`** | List all states containing the letter "a". |
| **10**      | **Get a state** | Print a state by name, or "Not found" if absent. |
| **11**      | **Add a new state** | Add a new State, "Louisiana". |
| **12**      | **Update a state** | Update the name of the state where id = 2. |
| **13**      | **Delete states** | Delete all states with names containing "a". |
| **14**      | **Cities in state** | Define a `City` class mapped to the `cities` table and list all cities grouped by state. |

## Example Usage
**Task 0 Example:** Listing All States
	./0-select_states.py username password database_name

## Tips for Success

    MySQLdb: Import and use MySQLdb to connect and interact with your MySQL database.
    SQLAlchemy: Use SQLAlchemy’s create_engine, sessionmaker, and ORM features to connect Python objects to your database.
    Avoid SQL Injection: Be cautious with user input in SQL queries. SQLAlchemy and MySQLdb provide parameterized queries to protect against SQL injection.
    Documentation: Document each module, class, and function in your code. Use __doc__ strings to describe their purpose.
    File Permissions: Make sure your Python scripts are executable with chmod +x.

## Author
This project was completed as part of the Holberton School curriculum by **Dijeont Jean-Paul**.