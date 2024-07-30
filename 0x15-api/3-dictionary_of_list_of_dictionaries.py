#!/usr/bin/python3
"""
A Script to fetch and export tasks for all users from a REST API
in JSON format
"""


import json
import requests


def main():
    """Fetch and export tasks for all users in JSON format."""
    response1 = requests.get('https://jsonplaceholder.typicode.com/users')
    response2 = requests.get('https://jsonplaceholder.typicode.com/todos')

    if response1.status_code != 200 or response2.status_code != 200:
        print("Error fetching data from the API")
        return

    users = response1.json()
    todos = response2.json()

    data = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_tasks = [
                {
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                for task in todos if task.get('userId') == user_id
        ]
        data[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()
