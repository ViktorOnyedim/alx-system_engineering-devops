#!/usr/bin/python3
"""Uses REST API, for a given employee ID, returns information about
his/her TODO list progress.
"""

import requests
from sys import argv


def main():
    emp_id = int(argv[1])

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(todos_url).json()
    users = requests.get(users_url).json()

    not_completed = 0
    completed = 0
    completed_titles = []

    for i in response:
        if i["userId"] == emp_id:
            if i['completed'] is True:
                completed += 1
                completed_titles.append(i['title'])
            else:
                not_completed += 1

    total_tasks = completed + not_completed

    for user in users:
        if user['id'] == emp_id:
            name = user['name']
            

    print(f"Employee {name} is done with tasks({completed}/{total_tasks}):")

    for title in completed_titles:
        print(f"\t {title}")


if __name__ == '__main__':
    main()
