#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """returns the total number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': \
               '0x16-api_advanced:v1.0.0 (by /u/Emergency-Cancel-250)'}
    r = requests.get(url, headers=headers).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
