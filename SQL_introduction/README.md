# SQL Introduction Project

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Tasks](#tasks)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Author](#author)

## Introduction
This project is designed to introduce the concepts of SQL and databases, specifically focusing on MySQL. The objective is to understand fundamental SQL commands and database management through practical tasks and exercises.

## Requirements
- **General**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All files must be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
  - All files should end with a new line.
  - All SQL queries should have a comment just before them.
  - All files should start with a comment describing the task.
  - All SQL keywords should be in uppercase (e.g., SELECT, WHERE).
  - A `README.md` file, at the root of the project directory, is mandatory.
  - The length of your files will be tested using `wc`.

## Tasks
The project includes the following tasks:
1. **List databases** - Write a script that lists all databases of your MySQL server.
2. **Create a database** - Write a script that creates the database `hbtn_0c_0` in your MySQL server.
3. **Delete a database** - Write a script that deletes the database `hbtn_0c_0`.
4. **List tables** - Write a script that lists all the tables of a database in your MySQL server.
5. **Create a first table** - Write a script that creates a table called `first_table`.
6. **Full description** - Write a script that prints the description of the `first_table`.
7. **List all in table** - Write a script that lists all rows of the `first_table`.
8. **Insert a new row** - Write a script that inserts a new row in the `first_table`.
9. **Count records** - Write a script that displays the number of records with `id = 89`.
10. **Create second table** - Write a script that creates a table `second_table` and adds multiple rows.
11. **List by best** - Write a script that lists all records ordered by score.
12. **Select the best** - Write a script that lists records with `score >= 10`.
13. **Update record** - Write a script that updates the score of `Bob`.
14. **Remove low scores** - Write a script that removes records with `score <= 5`.
15. **Compute average** - Write a script that computes the score average.
16. **Count by score** - Write a script that lists the number of records with the same score.
17. **Say my name** - Write a script that lists all records, excluding rows without a name value.

## Installation
To set up MySQL on Ubuntu 20.04 LTS, run:
```bash
sudo apt update
sudo apt install mysql-server
```
**Check the MySQL version:**
	mysql --version

## Usage
**Connect to your MySQL server:**
	sudo mysql

**Run your SQL scripts:**
	cat [script_name.sql] | mysql -hlocalhost -uroot -p

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## Author

This project was completed as part of the Holberton School curriculum by **Dijeont Jean-Paul**.