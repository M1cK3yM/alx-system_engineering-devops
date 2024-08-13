# Reddit API Query Project

## Description

This project contains Python scripts that interact with the Reddit API to perform various tasks such as retrieving the number of subscribers for a given subreddit and printing the titles of the first 10 hot posts listed for a subreddit. The scripts handle cases where the subreddit might not exist or might redirect to search results.

## Requirements

- **Operating System**: Ubuntu 20.04 LTS
- **Python Version**: Python 3.4.3 or higher
- **Allowed Editors**: `vi`, `vim`, `emacs`
- **Libraries**:
  - `requests`: Used for sending HTTP requests to the Reddit API.
- **Code Style**: Follows PEP 8 guidelines.

## Project Files

### 1. `0-subs.py`

This script contains the `number_of_subscribers` function, which queries the Reddit API and returns the number of subscribers for a given subreddit. If an invalid subreddit is provided, the function returns `0`.

- **Prototype**: `def number_of_subscribers(subreddit)`
- **Parameters**:
  - `subreddit` (string): The name of the subreddit to query.
- **Returns**:
  - The number of subscribers as an integer, or `0` if the subreddit is invalid.

#### Usage Example:

```bash
$ python3 0-main.py programming
756024

$ python3 0-main.py this_is_a_fake_subreddit
0

```

### 2. `1-top_ten.py`

This script contains the `top_ten` function, which prints the titles of the first 10 hot posts listed for a subreddit. If an invalid subreddit is provided, the function prints "None".

- **Prototype**: `def top_ten(subreddit)`
- **Parameters**:
  - `subreddit` (string): The name of the subreddit to query.
- **Returns**:
  - None

#### Usage Example:

```bash
$ python3 1-main.py programming

Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
HTTPS on Stack Overflow: The End of a Long Road
Spend effort on your Git commits
It's a few years old, but I just discovered this incredibly impressive video of researchers reconstructing sounds from video information alone
From the D Blog: Introspection, Introspection Everywhere
Do MVC like it’s 1979
GitHub is moving to GraphQL for v4 of their API (v3 was a REST API)
Google Bug Bounty - The 5k Error Page
PyCon 2017 Talk Videos

$ python3 1-main.py this_is_a_fake_subreddit
None
```
