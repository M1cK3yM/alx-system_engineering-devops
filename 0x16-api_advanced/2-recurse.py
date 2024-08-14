#!/usr/bin/python3
"""Module to recursively query the Reddit API and return titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list containing the titles of all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:myredditapp:v1.0.0 (by /u/Emergency-Cancel-250)"
    }
    params = {
        "after": after,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    hot_list.extend([child.get("data").get("title") for child in data.get("children", [])])

    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
