from pypinyin import lazy_pinyin
import pandas as pd

df = pd.read_table('qq.txt',sep='\t',header=None)
print(df.head(10))

def yinbiao(row):
    pinyin = lazy_pinyin(row)
    newrow = str(row) + str(",") + str(pinyin) + str(",1")
    return newrow

qq = df[0].map(lambda x: yinbiao(x))
qq.to_csv('qqpinyin.csv')