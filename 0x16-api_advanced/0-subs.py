#!/usr/bin/python3
"""
The script scraps the active subscribers from a subreddit
"""


import json
import requests
import sys


def get_subreddit_subs(subreddit):
    """
    The function gets the total number
    of subscribers from a subreddit
    Args:
        subreddit (str): The subreddit to query
    Returns:
        The total number of subscribers to the subreddit
    """

    try:
        base_url = f"https://www.reddit.com/r/{subreddit}/.json"
        request = requests.get(base_url, headers = {'User-agent':'alxSE'})
    except Exception as e:
        return 0

    sub_json = request.json()
    data = sub_json["data"]
    children = data["children"]

    return sum([child["data"]["subreddit_subscribers"] for child in children])


if __name__ == "__main__":
    subreddit = sys.argv[1]
    print(get_subreddit_subs(subreddit))
