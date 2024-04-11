#!/usr/bin/python3
"""
The script scraps the active subscribers from a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    The function gets the total number
    of subscribers from a subreddit
    Args:
        subreddit (str): The subreddit to query
    Returns:
        The total number of subscribers to the subreddit
    """
    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    request = requests.get(base_url,
                           headers={'User-agent': 'johnny@johnny Fedora Linux'},
                           allow_redirects=False)

    if request.status_code != 200:
        return 0

    sub_json = request.json()
    data = sub_json["data"]

    return data["subscribers"]
