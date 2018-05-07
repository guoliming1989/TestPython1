#coding:utf-8
#读文本文件，读取某范围的文本信息，如100-300行之间的内容，
# 我们是否可以使用类似列表切片的方式得到一个100-300行文件内容的生,读取文本最好的方式使用迭代的方式
f = open('test.txt')
lines = f.readlines()
for line in f:
    print line
f.seek(0)
# for line in f:#读取一行
#     print line

from itertools import  islice
islice(f,2,3)
for line in islice(f,2,3):#从多少行开始
    print line
l= range(20)
t = iter(l)
for x in islice(t,5,10):#迭代器的切片,会消耗原来的迭代对象
    print x
for x in t :
    print x