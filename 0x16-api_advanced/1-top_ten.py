#!/usr/bin/python3
""" 1. Top Ten """
from requests import get


def top_ten(subreddit):
    """ function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit. """
    headers = {"User-Agent": "javierandresgp"}
    try:
        general = get("https://www.reddit.com/r/{}.json?limit=10&sort=hot"
                      .format(subreddit), headers=headers,
                      allow_redirects=False).json()
        specific = general.get("data").get("children")
        for i in specific:
            print(i.get("data").get("title"))
    except:
        print(None)
