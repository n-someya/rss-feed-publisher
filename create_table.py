#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from ConfigParser import SafeConfigParser
import sys
import datetime


DEFAULT_COFIG_PATH = "./config.ini"
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
DATABASE_CONN = config.get('database', 'conn')
DATABASE_TABLE = config.get('database', 'tablename')

Base = declarative_base()
engine = create_engine(DATABASE_CONN)


class Feed(Base):
    __tablename__ = DATABASE_TABLE
    id = Column("id", Text, primary_key=True)
    link = Column("link", Text)
    title = Column("title", Text)
    summary = Column("summary", Text)
    updated = Column("updated", TIMESTAMP, default=datetime.datetime.now)

    def __init__(self, id, link, title, summary):
        self.id = id
        self.link = link
        self.title = title
        self.summary = summary
        self.updated = datetime.now()

Base.metadata.create_all(engine)
