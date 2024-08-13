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

### 3. `2-recurse.py`

This script contains the `recurse` function, which prints the titles of the first 10 hot posts listed for a subreddit. If an invalid subreddit is provided, the function prints "None".

- **Prototype**: `def recurse(subreddit, hot_list=[])`
- **Parameters**:
  - `subreddit` (string): The name of the subreddit to query.
  - `hot_list` (list): A list of the titles of the first 10 hot posts.
- **Returns**:
  - None

#### Usage Example:

```bash
$ python3 2-main.py programming
6483

$ python3 2-main.py this_is_a_fake_subreddit
None
```

### 4. `100-count.py`

This script contains the count_words function, which queries the Reddit API recursively and counts the occurrences of specified keywords in the titles of hot articles for a given subreddit. The function prints the counts in descending order of frequency and alphabetically by keyword when frequencies are equal.

- **Prototype**: `def count_words(subreddit, hot_list=[])`
- **Parameters**:
  - `subreddit` (string): The name of the subreddit to query.
  - `hot_list` (list): A list of the titles of the first 100 hot posts.
- **Returns**:
  - Prints the counts of each keyword in descending order of frequency, and alphabetically if frequencies are the same.

#### Usage Example:

```bash
$ python3 100-main.py programming 'react python java javascript scala no_results_for_this_one'
java: 27
javascript: 20
python: 17
react: 17
scala: 4

$ python3 100-main.py programming 'JavA java'
java: 54

$ python3 100-main.py not_a_valid_subreddit 'python java'
```
