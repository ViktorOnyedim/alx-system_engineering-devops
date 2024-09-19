#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[], after=None):
    # set a custom user-agent to avoid potential api issues
    headers = {'User-Agent': 'MyAgent/01'}

    # base url for reddit api
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Add 'after' parameter if it's provided
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check if the subreddit is invalid
        if response.status_code in [404, 302]:
            return None

        # Raise exception for any other unsuccessful status code
        response.raise_for_status()

        data = response.json()

        posts = data['data']['children']
        hot_list.extend([post['data']['title'] for post in posts])

        # check if there are more pages
        after = data['data']['after']
        if after:
            # recursively call the function with the new 'after' value
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except request.RequestException:
        return None



