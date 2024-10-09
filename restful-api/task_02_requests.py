#!/usr/bin/python3
"""Module task_02_request: Define consuming and
processing data from an API using python"""


import requests
import csv


def fetch_and_print_posts():
    """fetche and print all post from JSONplaceholder"""

    responce = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {responce.status_code}")
    if responce.status_code == 200:
        posts = responce.json()

        for post in posts:
            print(post['title'])
    else:
        print("Failed to retrieve posts.")


def fetch_and_save_posts():
    """Fetches posts from JSONPlaceholder and saves them to a CSV file."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        posts_data = []
        for post in posts:
            posts_data.append(
                {'id': post['id'],
                 'title': post['title'],
                 'body': post['body']})

        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_data)

        print("Posts saved to posts.csv")
    else:
        print("Failed to retrieve posts")
