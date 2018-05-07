#coding:utf-8
from random import randint,sample
#如何快速找到多个字典中的公共键（key），统计每一场比赛都有进球的球员,构建三轮的数据
t1 = sample('abcdefg',3)
t2 = sample('abcdefg',randint(3,6))
s1 ={x:randint(1,4) for x in t1}
s2 ={x:randint(1,4) for x in t2}
s3 ={x:randint(1,4) for x in t2}
res = []
#公共方法
for k in s1:
    if k in s2 and k in s3:
        res.append(k)
print res

#利用集合的操作方式，使用viewkeys()方法，得到一个字典的keys的集合,
# 然后使用集合的交集操作
#使用map函数
s1.viewkeys()
s2.viewkeys()
s3.viewkeys()
data2 = s1.viewkeys()&s2.viewkeys()&s3.viewkeys()
print data2
print map(dict.viewkeys,[s1,s2,s3])
data3 = reduce(lambda a,b:a&b ,map(dict.viewkeys,[s1,s2,s3]))
print data3


