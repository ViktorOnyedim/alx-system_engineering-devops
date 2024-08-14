#!/usr/bin/python3
"""
    Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my_alx:com.api_advanced:v1.0.0 (by /u/Do    wntown-Baby6380)'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        # Parse json data
        data = response.json()
        # get children object that contains the posts
        posts = data["data"]["children"]
        
        if posts:
            for i, post in enumerate(posts):
                if i < 10:
                    print(post['data']['title'])
                else:
                    break
    else:
        print("None")
        return
