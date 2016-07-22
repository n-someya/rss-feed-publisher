#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import time
# from datetime import datetime
import pandas as pd
from mattermost_client import mattermost_cl
import logging
import re
from ConfigParser import SafeConfigParser
import sys
from sqlalchemy import create_engine

DEFAULT_COFIG_PATH = "./config.ini"

tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
logger = logging.getLogger(__name__)


def main():

    try:
        param = sys.argv
        config_file = param[1]
    except IndexError:
        print("Use default config file(./config.ini)")
        print("If you specify original config file,")
        print("Usage: feedget.py [config file path]")
        config_file = DEFAULT_COFIG_PATH

    config = SafeConfigParser()
    config.read(config_file)

    MATTERMOSTURL = config.get('mattermost', 'url')
    RSS_URL = config.get('rss', 'url')
    MATTERMOST_USER = config.get('mattermost', 'username')
    GETFEED_INTERVAL = float(config.get('rss', 'interval'))
    SENDMESSAGE_INTERVAL = float(config.get('mattermost', 'interval'))
    DATABASE_CONN = config.get('database', 'conn')
    DATABASE_TABLE = "feed"

    mmc = mattermost_cl.MatterMostClient(MATTERMOSTURL)

    # Get First RSS feed. TODO: Get id from database
    print("Start get feed from %s" % (RSS_URL))
    feed = feedparser.parse(RSS_URL)
    initial_entries = pd.DataFrame(feed.entries)
    already_print_feeds = pd.Series(initial_entries['id'])
    # connect database
    engine = create_engine(DATABASE_CONN)

    while True:
        time.sleep(GETFEED_INTERVAL)
        feed = feedparser.parse(RSS_URL)
        entries = pd.DataFrame(feed.entries)
        new_entries = entries[~entries['id'].isin(already_print_feeds)]
        if not new_entries.empty:
            for key, row in new_entries.iterrows():
                feedinfo = "[**%s**](%s)\n\n>%s" % (row['title'],  row['link'], tag_re.sub('', row['summary']))
                mmc.send_message(feedinfo, username=MATTERMOST_USER)
                time.sleep(SENDMESSAGE_INTERVAL)
            # Store database
            stored_entries = new_entries.ix[:, [
                "id", "link", "title", "summary", "updated"]]
            stored_entries.to_sql(DATABASE_TABLE, engine, index=False, if_exists='append')
        # TODO: get already_print_feeds from database
        already_print_feeds = already_print_feeds.append(new_entries['id'])

if __name__ == "__main__":
    main()
