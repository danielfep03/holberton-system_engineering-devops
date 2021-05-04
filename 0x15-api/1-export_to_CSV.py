#!/usr/bin/python3
'''Script that use an API to show information about his Todo list progress'''
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + 'users?id=' + argv[1]
    todos_url = url + 'todos?userId=' + argv[1]

    employee = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    with open('{}.csv'.format(argv[1]), mode='w', encoding='utf-8') as file:
        for task in employee:
            for todo in todos:
                file.write('\"{}\",\"{}\",'.format(task['id'],
                                                   task['username']))
                file.write('\"{}\",\"{}\"\n'.format(todo['completed'],
                                                    todo['title']))
