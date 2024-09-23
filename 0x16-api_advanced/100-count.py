#!/usr/bin/python3
"""
Function to count words in all hot posts of a given Reddit subreddit.
"""

from collections import Counter
import re
import requests

def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    """
    if word_counts is None:
        word_counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title'].lower()
        words = re.findall(r'\b[\w]+\b', title)
        for word in words:
            if word.lower() in (w.lower() for w in word_list):
                word_counts[word.lower()] += 1

    after = data['data']['after']
    if after:
        return count_words(subreddit, word_list, after, word_counts)
    else:
        sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
