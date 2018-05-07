#coding:utf-8
#s收集到1g数据后存储在做数据分析，最终只保存分析结果，这样很大的临时文件如果
#常驻内存，将会消耗很大的内存资源，我们可以将临时文件存储在外存中，临时文件不用命名，且关闭后会自动删除
#使用tempfile#
from tempfile import TemporaryFile,NamedTemporaryFile
f =TemporaryFile()
f.write('abskjdhf'*10000)#临时文件的使用
f.seek(0)
print f.read(100)

#能在文件系统中找到的临时文件,临时文件关闭后自动删除
nft =NamedTemporaryFile()
print nft.name
nft = NamedTemporaryFile(delete=False)#不自动删除


