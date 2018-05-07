#coding:utf-8
#如何将json的数据转化为标准的
import requests
import  json
#录音
l=[1,2,'abc',{'name':'bob','age':13}]
print json.dumps(l)
print json.dumps(l,separators=[',',':'])
d={'b':None,'a':5,'c':'abc'}
print json.dumps(d)

json.dumps(d,sort_keys=True)#排序
#如何将json对象转化为列表
