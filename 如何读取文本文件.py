#coding:utf-8
#字符串语义的变化Python2  str  ---byte   unicode  --str
#写入文件前对Unicode编码，读入文件后对二进制字符解码
#open函数指定't文本模式，endcoding指定编码格式
print ord('a')
#Python2中字符串为字节编码
#Python3
s=u'你好'
#print s.encode('utf8')
#print s.encode('gbk')#编码与解码要使用同一的形式

f =open('py.txt','w')
f.write(s.encode('utf8'))
f.close()

f=open('py.txt','r')
t = f.read()
print t


#python 3zz自动编码和解码
f = open('test.txt','w')
s='你好'
f.write(s)
f.close()
#自动编程和解码
f = open('test.txt','wt')
f.write('你好 我爱编程')
f.close

f = open('test.txt','rt')
print (f.read())






