#coding:utf-8
from urllib import urlretrieve
#urlretrieve('http://table.finance.yahoo.com/table.cvs?s=000001.sz','pingan.csv')
import csv
rf = open('test.csv','rb')
reader = csv.reader(rf)
print reader.next()

#写文件
wf =open('pingan_copy.csv','wb')
writer = csv.writer(wf)
writer.writerow(['date','open','high','low','close','volume','adjclose'])#写入文件
wf.flush()
#需求：将记录中的带有条件的记录存储在另外的一张表中
import csv
with open('pingan.csv','rb') as rf:
    reader = csv.reader(rf)
    with open('pingan2.csv','wb') as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        writer.writerow(headers)
        for row in reader:
            if row[0] <'2016-01-01':
                break
            if int(row[5])>=50000:
                writer.writerow(row)

print 'end'



