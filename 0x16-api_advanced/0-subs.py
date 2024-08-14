#!/usr/bin/python3
"""
To get the total number of subscribers in a subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns total number of ubscribers in a subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {'User-Agent': 'Custom User-Agent for Subscriber Count'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return (0)
    except requests.RequestException:
        return (0)
