#!/usr/bin/python3
"""Uses REST API, for a given employee ID, returns information about
his/her TODO list progress.
"""

import requests
from sys import argv

def main():
    emp_id = int(argv[1])

    url = "https://jsonplaceholder.typicode.com/todos"
    
    response = requests.get(url)
    response_json = response.json()

    not_completed = 0
    task_completed = 0
    completed_titles = []

    for i in response_json:
        if i["userId"] == emp_id:
            if i['completed'] == True:
                task_completed += 1
                completed_titles.append(i['title'])
            else:
                not_completed += 1

    total_tasks = task_completed + not_completed

    print(f"Employee X is done with tasks({task_completed}/{total_tasks}):")
    for title in completed_titles:
        print(f"\t {title}")

if __name__ == '__main__':
    main()
