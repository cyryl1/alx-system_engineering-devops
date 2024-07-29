#!/usr/bin/python3
""""
A Script to fetch and display completed tasks for a user
from a REST API
"""

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

    EMPLOYEE_NAME = user.get('name')
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    task_titles = [item["title"] for item in tasks if item.get("completed")]
    NUMBER_OF_DONE_TASKS = len(task_titles)

    print(
            "Employee {} is done with tasks({}/{}):"
            .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)
    )
    for title in task_titles:
        print("\t {}".format(title))


if __name__ == "__main__":
    main()
