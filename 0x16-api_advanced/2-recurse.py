#!/usr/bin/python3
"""
The script queries top ten reddits using a recursion function
"""


import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursively queries the Reddit
    API and returns the titles of
    the first 10 posts or None for invalid subreddits.

    Args:
        after:
        subreddit: The name of the subreddit to query.
        hot_list (list, optional): Accumulates titles across
        recursive calls. Defaults to [].

    Returns:
        list: A list of titles from the top 10
        posts or None if the subreddit is invalid.
    """
    base_url = ("https://www.reddit.com/r/{}/hot.json"
                .format(subreddit))
    after = after
    request = requests.get(base_url,
                           headers={'User-Agent': 'johnny@johnny'},
                           params={'after': after},
                           allow_redirects=False)

    if request.status_code == 200:
        data = request.json()

        # Check for valid data structure before accessing children
        if "data" in data and "children" in data["data"]:
            children = data["data"]["children"]

            hot_list.extend([child["data"]["title"] for child in children])
            print(len(hot_list))

            # Check for "after" parameter indicating more pages
            if "after" in data["data"]:
                # Recursive call for next page
                return recurse(subreddit, hot_list, data["data"]["after"])
            else:
                return hot_list  # Return accumulated titles
        else:
            return None  # Invalid data structure, likely not a subreddit

    elif request.status_code == 302:  # Handle potential redirect
        return None

    else:  # Other error cases
        print(f"Error: {request.status_code}")
        return None
