#!/usr/bin/python3
'''Script that use an API to show information about his Todo list progress'''

import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + 'users'
    todos_url = url + 'todos'
    my_dict = {}
    task = {}
    my_list = []

    employees = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    for employee in employees:
        for todo in todos:
            if todo['userId'] == employee['id']:
                task['task'] = todo['title']
                task['completed'] = todo['completed']
                task['username'] = employee['username']
                my_list.append(task)
                task = {}
        my_dict[employee['id']] = my_list
        my_list = []

    with open('todo_all_employees.json', mode='w', encoding='utf-8') as file:
        json.dump(my_dict, file)
