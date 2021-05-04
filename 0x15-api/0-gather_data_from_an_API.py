#!/usr/bin/python3
'''Script that use an API to show information about his Todo list progress'''
from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + 'users?id=' + argv[1]
    todos_url = url + 'todos?userId=' + argv[1]
    list_done = []
    task_counter = 0
    done = 0

    employee = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    for task in todos:
        if task['completed'] is True:
            list_done.append(task['title'])
            done += 1
        task_counter += 1

    print('Employee {} is done with tasks({}/20):'.format(employee[0]['name'],
                                                          done))
    print('\t {}'.format('\n\t '.join(list_done)))
