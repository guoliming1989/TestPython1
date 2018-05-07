#coding:utf-8
#学生信息数据量很大减少存储使用元祖存储，对每一个学生信息表示为：
#使用c语言的枚举类型或者是宏定义，使用常量的定义
from collections import namedtuple
# NAME =0
# AGE=1
# SEX =2
# EMAIL =3
# NAME,AGE,SEX,EMAIL = xrange(4)
# student =('jim',10,'male','jim@gmail.com')
# print student[NAME]

#使用标准库中的collections.namedtuple替代内置的tuple

# 定义一个namedtuple类型User，并包含name，sex和age属性。
User = namedtuple('User', ['name', 'sex', 'age'])
# 创建一个User对象
user = User(name='kongxx', sex='male', age=21)
user1 = User('jim',1,3)
#直接使用类属性的方式访问元祖
print user.name
print user1
print user
print  isinstance(user,tuple)
