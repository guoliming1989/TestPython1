#coding:utf-8
from random import randint
from collections import Counter
import re
data = [randint(0,20) for _ in xrange(30)]
print data
#统计的结果为一个字段
c = dict.fromkeys(data,0)
for x in data:
    c[x] +=1
print c
c2 = Counter(data)
m = c2.most_common(3)#出现频度最高的书
print m

txt = open('codingStyle').read()#读入文件使用正则表达式，对词
c3 = Counter(re.split('\w+',txt))#使用非字母作为分割符，分割为列表
c3.most_common(10)#10个单词进行统计