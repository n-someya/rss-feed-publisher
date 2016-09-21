# IPython log file

from sqlalchemy import import create_engine
import MeCab
import pandas as pd
conn = "sqlite:///tmp/db.sqlite3"
engine = create_engine(conn)
articles = pd.read_sql_query("select * from feedredirector_article where feed_id = 1;", engine)
mecab = MeCab.Tagger("mecabrc")
dics=[]
for summary in articles['summary']:
    for word in mecab.parse(summary).split("\n")[0:-2]:
        if word.split("\t")[1].split(",")[0] == "名詞":
            dics.append(word.split("\t")[0]

dics
word_counter = Counter(dics)
from collections import Counter
word_counter = Counter(dics)
for word, cnt in word_counter.most_common()[0:30]:
    print (word, cnt)

