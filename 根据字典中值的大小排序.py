#coding:utf-8
sorted([9,1,2,8,5])
from random import randint,sample
data = {x: randint(60,100) for x in 'xyzabc'}
print data
sorted(data)
print data
#按照成绩来排序,利用元祖来排序，元祖的比较是先比较第0个元素，然后比较第1个元素
#利用zip函数
data.keys()
data.values()
data2 = zip(data.itervalues(),data.iterkeys())#使用迭代版本

print data.items()
data3 =sorted(data.items(),key=lambda x:x[1])#使用字典中的第一个值来排序
print data3


#如何快速找到多个字典中的公共键（key），统计每一场比赛都有进球的球员
t1 = sample('abcdefg',3)
t2 = sample('abcdefg',randint(3,6))









