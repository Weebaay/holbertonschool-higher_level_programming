# SQL - More Queries

## Description

This project is focused on learning advanced SQL concepts like user management, privileges, table constraints, and working with multiple tables using joins, subqueries, and more.

### Learning Objectives

By the end of this project, you will be able to:
- Create MySQL users and manage their privileges.
- Understand and use **PRIMARY KEY** and **FOREIGN KEY** constraints.
- Apply **NOT NULL** and **UNIQUE** constraints.
- Retrieve data from multiple tables in a single query using **JOIN** and **UNION**.
- Write subqueries for complex queries.

## Setup

- **OS**: Ubuntu 20.04 LTS
- **MySQL**: 8.0 (Version 8.0.25)
  
To install MySQL:
```bash
sudo apt update
sudo apt install mysql-server
```
To connect to MySQL:
	sudo mysql

## Tasks

| Task Number | Task Name                      | Description                                                                                           |
|-------------|---------------------------------|-------------------------------------------------------------------------------------------------------|
| Task 0      | My Privileges!                  | Write a script that lists all privileges of `user_0d_1` and `user_0d_2` on your MySQL server.          |
| Task 1      | Root User                       | Create a MySQL user `user_0d_1` with all privileges on the server.                                     |
| Task 2      | Read User                       | Create the database `hbtn_0d_2` and user `user_0d_2` with **SELECT** privilege on this database.       |
| Task 3      | Always a Name                   | Create a table `force_name` with a **NOT NULL** constraint on the `name` column.                       |
| Task 4      | ID Can't Be Null                | Create a table `id_not_null` where the `id` column has a default value of `1` and is **NOT NULL**.     |
| Task 5      | Unique ID                       | Create a table `unique_id` where the `id` column is **UNIQUE** and has a default value of `1`.         |
| Task 6      | States Table                    | Create the database `hbtn_0d_usa` and a table `states` with an `id` (AUTO_INCREMENT, PRIMARY KEY) and a `name` column. |
| Task 7      | Cities Table                    | Create a table `cities` with `id` (AUTO_INCREMENT, PRIMARY KEY), `state_id` (FOREIGN KEY), and `name`. |
| Task 8      | Cities of California            | Write a query to list all cities in California from the `hbtn_0d_usa` database.                        |
| Task 9      | Cities by States                | List all cities and their corresponding states from `hbtn_0d_usa` database using a **JOIN**.           |
| Task 10     | Genre ID by Show                | List all shows in `hbtn_0d_tvshows` with at least one genre linked.                                    |
| Task 11     | Genre ID for All Shows          | List all shows from `hbtn_0d_tvshows`, including those without any genres (show **NULL** for missing genres). |
| Task 12     | No Genre                        | List all shows from `hbtn_0d_tvshows` that have no genres linked.                                      |
| Task 13     | Number of Shows by Genre        | List all genres and the number of shows linked to each genre in `hbtn_0d_tvshows`.                     |
| Task 14     | My Genres                       | List all genres of the show "Dexter" from `hbtn_0d_tvshows`.                                           |
| Task 15     | Only Comedy                     | List all Comedy shows in `hbtn_0d_tvshows`.                                                            |
| Task 16     | List Shows and Genres           | List all shows and their corresponding genres from `hbtn_0d_tvshows`, showing **NULL** for shows without genres. |

## Author
This project was completed as part of the Holberton School curriculum by **Dijeont Jean-Paul**.