#coding:utf-8
#实际案例
#案例：过滤掉用户文本输入的多余的空白字符串，' nuck2008@gmail.com '
#  过滤掉windows下文本的'\r''hello world \r\n'

#过滤掉文本的Unicode组合的符号
#方法一：使用strip(),lstrip(),rstrip()去掉字符串二端的字符
#方法二：删除单个固定位置的字符，使用切片+拼接的方法
#方法三：字符串的replace()方法或者正则表达式re.sub删除任意位置的字符
#方法四：字符串translate()方法，可以删除多种不同的字符
#使用replace()方法或者正则表达式
#使用translate()方法
s = ' nuck2008@gmail.com '
print s.strip()
print s.rstrip()
s2= '---abc++'
print s2.strip('-+')

#使用切片加上拼接的方式
s3='abc:123'
print s3[:3]+s3[4:]

#使用字符串的替换方法或者正则表达式
s4 =r'\manc\m123\mxyz'
t2 = s4.replace('\m','')
print t2

#字符串替换
s = '\tabc\t123\trop\r'
import re
print re.sub('[\t\r]','',s)

#使用translate方法,字符映射的方式
s='abc1232xyz'
import string
string.translate('abcxyz','xyzabc')




