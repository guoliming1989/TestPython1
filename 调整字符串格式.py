#coding:utf-8
#判断字符串是否以字符串b开头或结尾，判断网络地址是否以http开头  如编写程序sh文件加上用户可执行权限
#解决方案  字符串的str.
import os,stat
s='g.sh'
print s.endswith('.sh')
s.endswith(('.sh','.py'))#只能为元祖
test1 =[name for name in os.listdir('.') if name.endswith(('.sh','.py'))]#过滤文件
print test1
os.stat('e.py')
