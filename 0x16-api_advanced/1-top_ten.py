#!/usr/bin/python3
"""Function to display the top 10 hot posts from a specified Reddit subreddit."""
import requests

def top_ten(subreddit):
    """Print the titles of the top 10 hot posts from a specified subreddit."""
    api_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "python:myredditapp:v2.0.0 (by /u/Emergency-Cancel-250)"
    }
    query_params = {
        "limit": 10
    }
    response = requests.get(api_url, headers=headers, params=query_params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    posts_data = response.json().get("data")
    [print(post.get("data").get("title")) for post in posts_data.get("children")]

