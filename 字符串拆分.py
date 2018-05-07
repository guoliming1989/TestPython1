#coding:utf-8
# s='ab;cd|edf|hg|hi,,jk|mn\topq;rst,uvw\txyz'
#其中<,>,<;>都是分隔符
#解决方案：连续使用str.split()方法，每次处理一种分隔符
#第二种方法是使用正则表达式，一次性拆分字符串
s = 'sdfsdkjfn 928309 0.0 skdj fns/jj R+ 12:5 '
test = s.split()
print test

s='ab;cd|edf|hg|hi,jk|mn\topq;rst,uvw\txyz'
s1 = s.split(';')
print s1
print map(lambda x: x.split('|'),s1) #遍历列表中的每一项，对每一项分割，变成一个二维列表

t =[]
map(lambda x: t.extend(x.split('|')),s1)#将列表扩展
print t
res = t
t=[]
map(lambda x: t.extend(x.split(',')),res)
print t

#如果存在二个,,要对结果的null字符串过滤
def mySplit(s,ds):
    res =[s]
    for d in ds:
        t =[]
        map(lambda x: t.extend(x.split(d)), res)
        res = t
    return [ x for x in res if x]#过滤掉null的字符串

print mySplit(s,';,|\t')
#正则表达式
import re
s2 = re.split('[,;\t|]+',s)
print s2

#如何调整字符串中文本的格式，其中的日期格式为'yyyy-mm-dd:2016-05-23改成05/23/2016'字符串替换的问题
s3 = '2016-05-23 skdnfsk skdjfnksd lsndlfn sldnflks'
print re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',s3)#主括号，主1、主2、主3,选取组


