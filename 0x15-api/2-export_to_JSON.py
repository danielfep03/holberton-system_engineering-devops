#!/usr/bin/python3
'''Script that use an API to show information about his Todo list progress'''
import requests
from sys import argv
import json

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + 'users?id=' + argv[1]
    todos_url = url + 'todos?userId=' + argv[1]
    task_list = []
    my_dict = {}
    my_dict[argv[1]] = []

    employee = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    for todo in todos:
        task = {}
        task['task'] = todo['title']
        task['completed'] = todo['completed']
        task['username'] = employee[0]['username']
        my_dict[argv[1]].append(task)
    with open('{}.json'.format(argv[1]), mode='w', encoding='utf-8') as file:
        json.dump(my_dict, file)
