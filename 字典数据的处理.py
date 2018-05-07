#coding:utf-8
from random import randint
import timeit
data =[randint(-10,10) for _ in xrange(10)]
print data

#保留正数，过滤掉负数
data1 = filter(lambda x:x>=0,data)
print data1

#使用列表解析的方式，迭代列表中的每一个元素
data2 = [x for x in data if x>=0]
print data2

#字典解析，同时迭代字典中的键和值
d ={x:randint(60,100) for x in xrange(1,21)}
print d
m={k:v for k,v in d.iteritems() if v>90}
print m

#集合解析
s = set(data)
print s
s1 ={x for x in s if x%3==0} #  如果x在s中并且x能被3整除
print s1
