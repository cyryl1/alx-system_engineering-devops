#!/usr/bin/python3
"""
Fetching data from Reddit API
"""

import requests


def count_words(subreddit, word_list, after='', word_count={}):
    """
    Recursively queries the Reddit API,
    parses the titles of all hot articles,
    and counts the occurrence of each keyword
    in word_list (case-insensitive).
    Prints the results in descending order by count,
    then alphabetically by word.
    """

    word_list = [word.lower() for word in word_list]

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Custom User-Agent for Keyword Counting'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
                url,
                headers=headers,
                params=params,
                allow_redirects=False
        )
        if response.status_code != 200:
            return

        data = response.json()
        articles = data['data']['children']

        for article in articles:
            title = article['data']['title'].lower()
            for word in word_list:
                a_word = word_count.get(word, 0) + title.split().count(word)
                word_count[word] = a_word

        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_words = sorted(
                    word_count.items(), key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_words:
                if count > 0:
                    print(f"{word}: {count}")

    except requests.RequestException:
        return
