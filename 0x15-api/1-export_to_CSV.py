#!/usr/bin/python3
""""
A Script to fetch and display completed tasks for a user
from a REST API
"""

import csv
import requests
import sys


def main():
    """Fetch an display complted tasks for a user."""
    if len(sys.argv) != 2:
        print("Usage: python3 <name_of_file.py> <employee_id>")
        return

    id = sys.argv[1]
    response1 = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    )
    response2 = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
    )

    if response1.status_code != 200 or response2.status_code != 200:
        print("Error fetching data from the API")
        return

    user = response1.json()
    tasks = response2.json()

    username = user.get('username')

    with open('{}.csv'.format(id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([
                id,
                username,
                task.get('completed'),
                task.get('title')
            ])


if __name__ == "__main__":
    main()
