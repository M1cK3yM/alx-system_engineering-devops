#!/usr/bin/python3
"""Module for counting specific keywords in hot articles of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """Recursively count and print sorted keywords from hot articles of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:myredditapp:v1.0.0 (by /u/YourUsername)"
    }
    params = {
        "after": after,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    children = data.get("children", [])

    for child in children:
        title = child.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            count = title.count(word.lower())
            if count > 0:
                counts[word.lower()] = counts.get(word.lower(), 0) + count

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    # Sorting and printing the results
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")
