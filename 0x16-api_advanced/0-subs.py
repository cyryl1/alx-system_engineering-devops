#!/usr/bin/python3
"""
To get the total number of subscribers in a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns total number of ubscribers in a subreddit
    If the subreddit is invalid, returns 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {'User-Agent': 'Custom User-Agent for Subscriber Count'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        return (data['data']['subscribers'])
    except (requests.exceptions.RequestException, KeyError, ValueError):
        return (0)
