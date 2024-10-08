#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. 
If an invalid subreddit is given, the function should return 0.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total no. of subscribers on a givven subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    headers = {
        'User-Agent': 'api_advanced/v1.0 (by /u/Downtown-Baby6380)'
    }
    res = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if res.status_code == 200:
        data = res.json()
        return data.get('data').get('subscribers')
    else:
        return 0
        
