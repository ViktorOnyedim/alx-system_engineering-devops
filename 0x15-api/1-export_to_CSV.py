#!/usr/bin/python3
"""Uses REST API, for a given employee ID, returns information about
his/her TODO list progress.
"""

import csv
import requests
from sys import argv


def main():
    emp_id = int(argv[1])

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"

    todos = requests.get(todos_url, params={"userId": emp_id}).json()
    user = requests.get(f"{users_url}/{emp_id}").json()
    name = user.get("username")

    filename = f"{emp_id}.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            task_completed = task.get('completed')

            writer.writerow([emp_id, name, task_completed, task.get('title')])


if __name__ == '__main__':
    main()
