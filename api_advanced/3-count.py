#!/usr/bin/python3
""""Doc"""
import requests


def count_words(subreddit, word_list, after="", wd_ct={}):
    """ "Doc"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}
    param = {"after": after}
    res = requests.get(url, headers=header, params=param)

    if res.status_code != 200:
        return

    json_res = res.json()  # chch
    after = json_res.get("data").get("after")
    has_next = after is not None
    hot_titles = []
    words = [word.lower() for word in word_list]

    if len(wd_ct) == 0:
        wd_ct = {word: 0 for word in words}

    hot_articles = json_res.get("data").get("children")
    for article in hot_articles:
        hot_titles.append(article.get("data").get("title"))

    # loop through all titles
    for i in range(len(hot_titles)):
        for title_word in hot_titles[i].lower().split():
            for word in words:
                if word.lower() == title_word:
                    wd_ct[word] = wd_ct.get(word) + 1

    if has_next:
        return count_words(subreddit, word_list, after, wd_ct)
    else:
        wd_ct = dict(filter(lambda item: item[1] != 0, wd_ct.items()))

        wd_ct = sorted(
            wd_ct.items(), key=lambda item: item[1], reverse=True
        )

        for i in range(len(wd_ct)):
            print("{}: {}".format(wd_ct[i][0], wd_ct[i][1]))
