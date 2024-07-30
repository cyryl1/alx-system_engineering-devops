#!/usr/bin/python3
"""
A Script to fetch and export tasks for a user
from a REST API in JSON format
"""


import json
import requests
import sys


def main():
    """Fetch and export tasks for a user in JSON format."""
    if len(sys.argv) != 2:
        print("Usage: python3 <filename.py> <employee id>")
        return

    user_id = sys.argv[1]
    response1 = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    )
    response2 = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user_id)
    )

    if response1.status_code != 200 or response2.status_code != 200:
        print("Error fetching data from the API")
        return

    user = response1.json()
    tasks = response2.json()

    username = user.get('username')

    tasks_list = [
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
            for task in tasks
    ]

    data = {user_id: tasks_list}

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()
