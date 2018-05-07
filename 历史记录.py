#coding:utf-8
#显示历史记录，容量为5的队列
from random import randint
from collections import deque
import pickle
history = deque([],5)
pickle.dump(history,open('history','w'))#存储历史记录文件
q2 = pickle.load(open('history','w'))
#q.append(1)#添加队列
N = randint(0,100)
def guess(k):
    if k==N:
        print 'right'
        return True
    if k<N:
        print '%s is less than N' %k
    else:
        print '%s is larger than N' % k
    return False
