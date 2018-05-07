#coding:utf-8
#如何让字典保持有序，答题越短成绩越优秀，
# 选手可以查询自己的成绩，可以按照顺序打印成绩,解决方案 有序的字典,按照进入字典的顺序遍历
from collections import OrderedDict
from random import randint
from time import time
d ={}
d['jim']=(1,35)
d['leo']=(2,37)
d['bob']=(3,40)
print d
d1 = OrderedDict()
d1['jim']=(1,35)
d1['leo']=(2,37)
d1['bob']=(3,40)
# for k in d1 :
#     print k
#test
test = OrderedDict()
players = list('abcdefgh')
start = time()
for i in xrange(8):
    raw_input()#用户输入
    p =players.pop(randint(0,7-i))
    end = time()
    print i+1,p,end-start
    test[p]=(i+1,end-start)

print
print '-'*20
for k in test:
    print k,test[k]
#按照进入的顺序打印成绩的排名