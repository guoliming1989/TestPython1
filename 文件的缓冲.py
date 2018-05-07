#coding:utf-8
#文件的内容很大，为了减少io操作，系统使用缓冲区将数据写入磁盘，达到一个快的大小写入
f = open('demo.txt','w')
f.write('abc')
f.write('+'*4093)#默认为4096个信号
f =open('demo2.txt','w',buffering=2048)
f.write('+'*1024)
f.close()

#行缓冲的行为
f=open('demo3.txt','w',buffering=1)#行缓冲的行为

#无缓冲的行为buffering=0

