#coding:utf-8
#情况：某班学生期末考试成绩语文数学英文分别存储在3个列表中，同时迭代三个列表，计算每个学生的总分（并行）
#某年级有4个班，某次开始每班英语成绩分别存储在4个列表中，依次迭代每个列表，统计全学年成绩高于90分的人数 （串行）
from random import randint
chines = [randint(60,100) for _ in xrange(40)]
math = [randint(60,100) for _ in xrange(40)]
eglishe = [randint(60,100) for _ in xrange(40)]
for i in xrange(len(math)):
    chines[i]+math[i]+eglishe[i]

m = zip([1,2,3,4],('a','b','c','d'))
print m
total =[]
for c ,m,e in zip(chines,math,eglishe):#并行的例子
    total.append(c+m+e)
print total

#串行的例子
from itertools import chain
chain([1,2,3,4],['a','b','c'])
e1 = [randint(60,100) for _ in xrange(42)]
e2 = [randint(60,100) for _ in xrange(43)]
e3 = [randint(60,100) for _ in xrange(39)]
count =0
for s in chain(e1,e2,e3):
    if s >90:
        count +=1
print count


