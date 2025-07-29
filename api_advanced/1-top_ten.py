#!/usr/bin/python3
"""
A module that prints the titles of the top
10 hot posts from a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    A function that fetches and prints the titles
    of the top ten hot posts from a subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(
        url,
        params={"after": None},
        allow_redirects=False,
        headers=headers,
    )

    if response.status_code != 200:
        print(None)
        return

    jsonData = response.json()
    data = jsonData["data"]["children"]
    for post in data:
        print(post.get("data", {}).get("title"))
