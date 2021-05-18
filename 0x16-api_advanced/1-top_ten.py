#!/usr/bin/python3
"""
Module that create a new functions
"""

import requests


def top_ten(subreddit):
    """ Function to get the 10 hot titles"""

    agent = {"user-agent": 'Juan/007'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    resp = (requests.get(url,
            headers=agent, allow_redirects=False))
    if resp.status_code != 200:
        print(None)
    rspjson = resp.json()
    if rspjson:
        data = rspjson.get('data')
        if data:
            children = data.get('children')
            if children:
                for number in children[:10]:
                    if number:
                        data2 = number.get('data')
                        if data2:
                            title = data2.get('title')
                            if title:
                                print(title)
