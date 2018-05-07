#coding:utf-8
#如何对字符串进行左右居中对齐，例子{'location':100.0,'smallcull':0.04}
#在Python中使用str.ljust(),str.rjust(),str.center()
#使用format()传递类似的参数
s= 'abc'
print s.ljust(20,'=')
print s.rjust(20,'=')
print s.center(20)
#使用format方法
format(s,'<20')
format(s,'>20')
format(s,'^20')
d={'location':100.0,'smallcull':0.04}
w = max(map(len,d.keys()))#拿到key的长度，然后设置左对齐，左右居中的对齐
for k in d:
    print k.ljust(w),':',d[k]


