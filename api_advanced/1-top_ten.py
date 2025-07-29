#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Return number of subscribers if @subreddit is valid subreddit.
    if not return 0."""

    headers = {
        'User-Agent': 'python:top_ten_script:v1.0 (by /u/Separate-Lion-614)'
    }
    subreddit_url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        if posts:
            for i in range(min(10, len(posts))):
                print(posts[i].get('data', {}).get('title'))
        else:
            print("OK")
    else:
        print("OK")
