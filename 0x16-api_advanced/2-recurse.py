#!/usr/bin/python3
"""Queries the Reddit API and
returns a list containing the
titles of all hot articles for
a given subreddit.

If no results are found for the
given subreddit, the function
should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Returns a list containing the titles of all
    hot articles for a given subreddit.
    """
    # Set the Default URL strings
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/hot.json'.format(base=base_url,
                                                     subreddit=subreddit)

    # Set an User-Agent
    user_agent = {'User-Agent': 'Python/requests'}

    # Set the Query Strings to Request
    payload = {'after': after, 'limit': '100'}

    # Get the Response of the Reddit API
    res = requests.get(api_uri, headers=user_agent,

