#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import time
# from datetime import datetime
import pandas as pd
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

    # Retlieve config data.
    MATTERMOSTURL = config.get('mattermost', 'url')
    RSS_URL = config.get('rss', 'url')
    MATTERMOST_USER = config.get('mattermost', 'username')
    GETFEED_INTERVAL = float(config.get('rss', 'interval'))
    SENDMESSAGE_INTERVAL = float(config.get('mattermost', 'interval'))
    DATABASE_CONN = config.get('database', 'conn')
    DATABASE_TABLE = config.get('database', 'tablename')

    # Connect database
    engine = create_engine(DATABASE_CONN)


    # Get First RSS feed. TODO: Get id from database
    print("Start get feed from %s" % (RSS_URL))
    already_print_feeds = pd.read_sql_query("select * from %s" % DATABASE_TABLE, engine)


    print already_print_feeds

if __name__ == "__main__":
    main()
