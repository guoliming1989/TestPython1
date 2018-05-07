#coding:utf-8
f=open('demo.war','rb')
info =f.read(44)#二进制文件
import struct
struct.uppack('h','\x01\02')
import array

