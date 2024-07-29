#!/usr/bin/python3
""""
A API request project
"""

import requests
import sys


id = sys.argv[1]
response1 = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id)
)
response2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
)
result1 = response1.json()
result2 = response2.json()

EMPLOYEE_NAME = result1['name']
TOTAL_NUMBER_OF_TASKS = len(result2)
task_titles = [item["title"] for item in result2 if item["completed"]]
NUMBER_OF_DONE_TASKS = len(task_titles)


print(
        "Employee {} is done with tasks({}/{}):"
        .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)
)

for title in task_titles:
    print("\t {}".format(title))
