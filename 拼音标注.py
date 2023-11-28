# 增加去除多余符号
# yaml的语法没有弄清楚，仍旧需要使用手工的方式去除某些
# 符号，同时也需要添加进去	这个隐藏的箭头符号


from pypinyin import lazy_pinyin
import pandas as pd
import csv

df = pd.read_table('Company-Shorter-Form28W.txt',sep='\t',header=None)
print(df.head(10))

def yinbiao(row):
    pinyin = lazy_pinyin(row)
    newrow = str(row) + str(",") + str(pinyin) + str(",1")
    return newrow

qq = df[0].map(lambda x: yinbiao(x))
qq.to_csv('CompanyNames.csv',header=False, index=False, sep="\t",quoting=csv.QUOTE_NONE,quotechar="",  escapechar="\\")