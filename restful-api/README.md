# RESTful API Project

## Overview
This project involves creating a RESTful API using Python. The API will be built using different technologies and frameworks, enabling students to understand the fundamentals of web services and API development.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Tasks](#tasks)
5. [Contributing](#contributing)
6. [License](#license)

## Prerequisites
- Python 3.x
- Pip

## Installation
Clone the repository:
	git clone 	https://github.com/Weebaay/holbertonschool-	higher_level_programming.git

Install required packages:
	pip install -r requirements.txt


## Usage

To run the API, use:
	python app.py

# Tasks

## 0. Basics of HTTP/HTTPS
**mandatory**  

**Background:**  
HTTP is the foundation of web communication, while HTTPS adds a security layer with SSL/TLS encryption.

**Objective:**  
- Differentiate between HTTP and HTTPS.
- Understand HTTP requests/responses structure.
- Recognize common HTTP methods and status codes.

**Resources:**  
- [MDN - Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)  
- [HTTP vs HTTPS](https://www.freecodecamp.org/news/http-vs-https/)  
- [HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

**Instructions:**
1. **Differentiate HTTP and HTTPS:**  
   Summarize differences, focusing on security. Optional: Use Wireshark to analyze HTTP/HTTPS traffic.
   
2. **Explore HTTP Structure:**  
   Inspect a webpage’s network activity. Check the “Headers” section for the first request to understand request/response structure.
   
3. **HTTP Methods and Status Codes:**  
   List four common methods (e.g., GET, POST) and five status codes (e.g., 404, 200) with brief descriptions and use cases.

**Hints:**  
- HTTPS encrypts data, protecting it from eavesdroppers.
- Status codes are grouped: 1xx (info), 2xx (success), 3xx (redirection), 4xx (client errors), 5xx (server errors).

---

## 1. Consume Data from an API Using curl
**mandatory**  

**Background:**  
curl is a command-line tool for transferring data via various protocols, often used to interact with APIs.

**Objective:**  
- Install and use curl.
- Construct basic API requests.

**Resources:**  
- [curl Documentation](https://curl.se/docs/)  
- [Using cURL with APIs](https://www.digitalocean.com/community/tutorials/how-to-use-curl)  
- [JSONPlaceholder API](https://jsonplaceholder.typicode.com)

**Instructions:**
1. **Install and Verify curl:**  
   Install curl, then run `curl --version`.

2. **Fetch Data:**  
   Retrieve posts: `curl https://jsonplaceholder.typicode.com/posts`.

3. **Headers and POST Requests:**  
   Fetch headers: `curl -I https://jsonplaceholder.typicode.com/posts`.  
   Make a POST request: `curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`.

**Hints:**  
- Use `-I` for headers, `-X` for methods, and `-d` for data in requests.

---

## 2. Consuming Data from an API Using Python
**mandatory**  

**Background:**  
Python’s requests library simplifies API interactions and JSON data manipulation.

**Objective:**  
- Use requests to send HTTP requests and process responses.
- Parse JSON and convert it to CSV.

**Resources:**  
- [Python Requests Library](https://requests.readthedocs.io/en/latest/)  
- [Working with JSON in Python](https://docs.python.org/3/library/json.html)  
- [JSONPlaceholder API](https://jsonplaceholder.typicode.com)

**Instructions:**
1. **Install Requests:**  
   Install using `pip install requests`.

2. **Basic Script:**  
   Fetch posts using `requests.get()` and print the status code.

3. **Functions:**
   - `fetch_and_print_posts()`: Fetch and print post titles.
   - `fetch_and_save_posts()`: Fetch posts and save to `posts.csv`.


	main_02_requests.py
	rom task_02_requests import fetch_and_print_posts, 			fetch_and_save_posts

	fetch_and_print_posts()
	fetch_and_save_posts()

## Author

This project was completed as part of the Holberton School curriculum by **Dijeont Jean-Paul**.