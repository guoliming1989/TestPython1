#coding:utf-8
#如迭代（3.0,4.0,0.2）可产生的序列，正向迭代：3.0,3.2,3.4.。。。序列的反向迭代
# l=[1,2,3,4,5]
# for x in reversed(l):
#     print x
#yield 相当于一个生成器，记录代码执行的位置，然后从下一次迭代从这个位置开始

class FloatRange:
    def __init__(self,start,end,step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):#正向迭代器
        t= self.start
        while t<=self.end:
            yield t
            t+=self.step

    def __reversed__(self):#反向迭代器
        t= self.end
        while t>=self.start:
            yield t
            t -= self.step


# for x in FloatRange(1.0,4.0,0.5):#正向迭代
#     print x

for x in reversed(FloatRange(1.0,4.0,0.5)):#反向迭代
    print x
