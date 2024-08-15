#!/usr/bin/python3
"""
A reddit app
"""

import requests


def top_ten(subreddit):
    """
    Prints title  for first ten hot posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Custom User-Agent for Top Ten Posts'}
    params = {'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
