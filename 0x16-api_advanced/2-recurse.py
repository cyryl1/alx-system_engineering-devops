#!/usr/bin/python3
"""
A reddit app
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all hot articles
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    headers = {'User-Agent': 'Custom User-Agent for Recursion'}

    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(
                url,
                headers=headers,
                params=params,
                allow_redirects=False
                )

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']

            for post in posts:
                hot_list.append(post['data']['title'])

            if after:
                return (recurse(subreddit, hot_list, after))
            else:
                return (hot_list)
        else:
            return (None)
    except requests.RequestException:
        return (None)
