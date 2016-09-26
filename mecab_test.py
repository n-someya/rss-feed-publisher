# IPython log file

from sqlalchemy import create_engine
from gensim import corpora
import MeCab
import pandas as pd
import pprint
import re
from collections import Counter

conn = "sqlite:///tmp/db.sqlite3"
engine = create_engine(conn)
articles = pd.read_sql_query("select * from feedredirector_article where feed_id = 1;", engine)
mecab = MeCab.Tagger("mecabrc")
dics=[]
docs=[]
docs_num = 0
for summary in articles['summary']:
    docs.append([])
    for word in mecab.parse(summary).split("\n")[0:-3]:
        if word.split("\t")[1].split(",")[0] == "名詞":
            if not re.match(r"[]",word.split("\t")[0])
            dics.append(word.split("\t")[0])
            docs[docs_num].append(word.split("\t")[0])
    docs_num += 1

# pprint.pprint(dics)
# pprint.pprint(docs)
word_counter = Counter(dics)
from collections import Counter
word_counter = Counter(dics)
for word, cnt in word_counter.most_common()[0:30]:
    print (word, cnt)

