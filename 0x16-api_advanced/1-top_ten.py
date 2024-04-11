#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 posts
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and returns the titles of the first 10 posts
    Args:
        subreddit:
        The name of the subreddit to query
    Returns:
        The titles of the first 10 posts
    """

    base_url = ("https://www.reddit.com/r/{}/top.json?limit=10"
                .format(subreddit))
    request = requests.get(base_url, headers={'User-Agent': 'johnny@johnny'},
                           allow_redirects=False)
    if request.status_code != 200:
        print("None")

    data = request.json()

    children = data['data']['children']

    for child in children:
        print(child["data"]["title"])
