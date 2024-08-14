#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a givven subreddit."""
    endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    headers = {'User-Agent': 'my_alx:com.api_advanced:v1.0.0 (by /u/Downtown-Baby6380)'}
    response = requests.get(endpoint, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        #data = response.json()
        data = response.json().get('data').get('subscribers')
        return data
    else:
        return 0


