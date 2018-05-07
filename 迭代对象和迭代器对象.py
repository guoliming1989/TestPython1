#coding:utf-8
#网络上抓取各个城市的气温信息并依次显示  北京：15-22 天津：17-22，用时访问的策略，抓取一条显示一条，可以使用for进行迭代
import requests
l=[1,2,3,4]
s='abcde'
for x in l:#实际上为调用l的迭代器对象
    print x
t =iter(l)#可迭代对象和迭代对象
print l.__iter__()#实际上内部调用迭代的方法
print t.next()

def getWeather(city):
    r = requests.get(u'http://wthrcd.etouch.cn/weather_mini?city='+city)
    data = r.json()['data']['forecast'][0]
    return '%s,%s,%s'%(city,data['low'],data['high'])

print getWeather(u'北京')






