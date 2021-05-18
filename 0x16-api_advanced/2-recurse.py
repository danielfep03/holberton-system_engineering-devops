#!/usr/bin/python3
"""
Module that create a new functions
"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """ Function that return a list of hot titles """

    agent = {"user-agent": 'Juan/007'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    payload = {"after": after}
    resp = (requests.get(url,
            headers=agent, allow_redirects=False, params=payload))
    if resp.status_code != 200:
        return None
    rspjson = resp.json()
    if rspjson:
        data = rspjson.get('data')
        if data:
            after = data.get('after')
            children = data.get('children')
            if children:
                for number in children:
                    if number:
                        data2 = number.get('data')
                        if data2:
                            title = data2.get('title')
                            if title:
                                hot_list.append(title)
    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list
