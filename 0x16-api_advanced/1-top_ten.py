#!/usr/bin/python3
"""
    Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hottest posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'my_alx:com.api_advanced:v1.0.0 (by /u/Downtown-Baby6380)',
    }
    params = {
        "limit": 10,
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    data = response.json().get("data")
    [print(post.get("data").get("title")) for post in data.get("children")]
