#coding:utf-8
#实现一个可迭代对象的类，它可以迭代出给定范围的素数,生成器对象
def f():
    print 'in f(),1'
    yield 1
    print 'in f(),2'
    yield 2
    print 'in f(),3'
    yield 3

g= f()
# print g.next()
# print g.next()
for  x in g:
    print x
print g.__iter__() is g;#返回迭代对象

class  PrimeNumbers:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def isPrimeNum(self,k):
        if k<2:
            return False
        for i in xrange(2,k):
            if k%i==0:
                return False
        return True
    def __iter__(self):    #将类的_iter_方法实现成生成器函数
        for k in xrange(self.start,self.end+1):
            if self.isPrimeNum(k):
                yield k

for x in PrimeNumbers(1,100):
    print x