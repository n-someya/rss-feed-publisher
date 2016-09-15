#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import time
# from datetime import datetime
import pandas as pd
from mattermost_client import mattermost_cl
import logging
import re
try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser

import sys
from sqlalchemy import create_engine

DEFAULT_COFIG_PATH = "./config.ini"
DATABASE_TABLE = "feedredirector_article"
FEED_TABLE = "feedredirector_feed"
USER_ID=1
SERVER_URL="http://10.125.75.43:8000/smartfeed/feed/{0}/{1}"

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

    # Retlieve config data.
    MATTERMOSTURL = config.get('mattermost', 'url')
    RSS_URL = config.get('rss', 'url')
    MATTERMOST_USER = config.get('mattermost', 'username')
    GETFEED_INTERVAL = float(config.get('rss', 'interval'))
    SENDMESSAGE_INTERVAL = float(config.get('mattermost', 'interval'))
    DATABASE_CONN = config.get('database', 'conn')

    # Connect Mattermost
    mmc = mattermost_cl.MatterMostClient(MATTERMOSTURL)
    # Connect database
    engine = create_engine(DATABASE_CONN)

    # Get id from database TODO: order datetime and limit num of records
    feed_id = pd.read_sql_query("select * from {0} where url = '{1}'".format(FEED_TABLE, RSS_URL), engine)['id'][0]

    print("Start get feed from %s" % (RSS_URL))
    already_print_feeds = pd.read_sql_query("select * from {0} where feed_id == {1}".format(DATABASE_TABLE, feed_id), engine)

    while True:
        time.sleep(GETFEED_INTERVAL)
        feed = feedparser.parse(RSS_URL)
        entries = pd.DataFrame(feed.entries)
        new_entries = entries[~entries['link'].isin(already_print_feeds['link'])]
        if not new_entries.empty:
            # Store database
            stored_entries = new_entries.ix[:, [
                "link", "title", "summary", "updated"]]
            stored_entries['feed_id'] = feed_id
            stored_entries.to_sql(DATABASE_TABLE, engine, index=False, if_exists='append')
            for key, row in new_entries.iterrows():
                article = pd.read_sql_query("select * from {0} where feed_id == {1} and link == '{2}'".format(DATABASE_TABLE, feed_id, row['link']), engine)
                feedinfo = "[**{0}**]({1})\n\n>{2}".format(row['title'], SERVER_URL.format(article['id'][0], USER_ID), tag_re.sub('', row['summary']))
                print(feedinfo)
                # mmc.send_message(feedinfo, username=MATTERMOST_USER)
                time.sleep(SENDMESSAGE_INTERVAL)

        # get already_print_feeds from database
        already_print_feeds = pd.read_sql_query("select * from {0} where feed_id == {1}".format(DATABASE_TABLE, feed_id), engine)


if __name__ == "__main__":
    main()
