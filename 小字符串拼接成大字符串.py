#coding:utf-8
#自定义网络参数hwDe,向服务器传输固定的参数，想['<0112>',"<32>",",."]
s1 = 'abcdefg'
s2 ='23y8989'
print s1+s2
print s1>s2
t1 =["<0113>","<0112>","<60>","<100.0>","<500.0>"]
s=''
for p in t1:
    s+= p
    print s
print s
#不存在临时变量的替换,如果拼接的字符串很多时，可以使用join对象来使用
t2 =';'.join(['abc','123','xyz'])
print t2

t3 =''.join(['abc','123','xyz'])
print t3

l =['abc',123,45,'xyz']
t4 = ''.join([str(x) for x in l])
print t4

t5 = ''.join((str(x) for x in l))
print t5
