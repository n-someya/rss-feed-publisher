#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import time
# from datetime import datetime
import pandas as pd
from mattermost_client import mattermost_cl as mmc

MATTERMOSTURL = "http://10.125.75.11:8065/hooks/qs4uzy4b1py98qjpiut93sewzw"
RSS_URL = "http://b.hatena.ne.jp/hotentry/it.rss"
MATTERMOST_USER = 'はてブTECHフィード'

mmc = mmc.MatterMostClient(MATTERMOSTURL)

already_print_feeds = pd.Series([])

print("Start get feed...")

while True:
    time.sleep(600)
    feed = feedparser.parse(RSS_URL)
    entries = pd.DataFrame(feed.entries)
    new_entries = entries[~entries['id'].isin(already_print_feeds)]

    if not new_entries.empty:
        for key, row in new_entries.iterrows():
            feedinfo = "[**%s**](%s)\n\n>%s" % (row['title'],  row['link'], row['summary'].replace("|", ":"))
            mmc.send_message(feedinfo, username=MATTERMOST_USER)
            time.sleep(10)

    already_print_feeds = already_print_feeds.append(new_entries['id'])
    break
