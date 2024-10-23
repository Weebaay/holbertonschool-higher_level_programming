# HBnB Application - User Management API

## Table of Contents
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Installation and Setup](#installation-and-setup)
4. [API Endpoints](#api-endpoints)
   - [Create a User](#create-a-user)
   - [Retrieve a User by ID](#retrieve-a-user-by-id)
   - [Retrieve the List of Users](#retrieve-the-list-of-users)
   - [Update a User](#update-a-user)
5. [Expected Response Formats](#expected-response-formats)
6. [Testing the API](#testing-the-api)
7. [Resources](#resources)

## Introduction

The **HBnB User Management API** allows for the creation, retrieval, and update of users. This API is built with **Flask-RESTx** and follows RESTful conventions. CRUD operations for user management are handled, excluding the DELETE operation.

This project is part of the broader HBnB application, which is a housing reservation platform. This document will guide you through the setup process, the available endpoints, and how to interact with the API.

## Project Structure

```bash
hbnb/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── users.py        # User API endpoints
│   ├── models/
│   │   └── user.py             # User model definition
│   ├── services/
│   │   └── facade.py           # Facade pattern to interact with business logic
│   └── persistence/
│       └── repository.py       # In-memory repository for object persistence
├── config.py                   # Application configuration
├── run.py                      # Entry point to run the Flask app
├── requirements.txt            # Python dependencies
└── tests/                      # Unit tests for the API and models
```


## Installation and Setup

To run the application, follow these steps:

    Clone the repository:

		git clone https://github.com/Weebaay/holbertonschool-higher_level_programming.git

		cd holbertonschool-hbnb/part2/hbnb

Create a virtual environment:

		python3 -m venv venv
		source venv/bin/activate

Install the dependencies:

		pip install -r requirements.txt

Run the application:

    python3 run.py

The application will now be running on http://127.0.0.1:5000/.

## API Endpoints
### Create a User

    URL: /api/v1/users/
    Method: POST
    Description: Registers a new user.
    Request Body:

	{
  		"first_name": "John",
  		"last_name": "Doe",
  		"email": "john.doe@example.com"
	}

	Success Response:

    	Code: 201 Created

## Expected Response Formats

All responses from the API will be in JSON format. Ensure that the Content-Type header is set to application/json in your requests.
### Testing the API

You can test the API using Postman or cURL. Here are some examples of cURL commands for testing:
## Create a User


	curl -X POST http://127.0.0.1:5000/api/v1/users/ \
	-H "Content-Type: application/json" \
	-d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}'

**Retrieve a User by ID**


	curl -X GET http://127.0.0.1:5000/api/v1/users/<user_id>

**Retrieve the List of Users**

	curl -X GET http://127.0.0.1:5000/api/v1/users/

**Update a User**

	curl -X PUT http://127.0.0.1:5000/api/v1/users/<user_id> \
	-H "Content-Type: application/json" \
	-d '{"first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com"}'

**Resources**

    Flask-RESTx Documentation
    Testing REST APIs with cURL
    Designing RESTful APIs

## Author

This project was completed as part of the Holberton School curriculum by **Dijeont Jean-Paul**.