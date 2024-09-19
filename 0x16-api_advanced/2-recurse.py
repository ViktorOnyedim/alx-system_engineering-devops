#!/usr/bin/python3
"""
Using reddit's API recursively
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returning top post titles recursively"""
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, params=parameters, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        after = data.get("after")
        all_titles = data.get("children")
        
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))

        # Continue recursion if there is another page of posts
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
