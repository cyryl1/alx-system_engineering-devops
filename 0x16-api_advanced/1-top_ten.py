#!/usr/bin/python3
"""
A reddit app
"""

import requests

def top_ten(subreddit):
    """
    Prints title  for first ten hot posts
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    headers = {'User-Agent': 'Custom User-Agent for Top Ten Posts'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
