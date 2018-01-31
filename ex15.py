#coding:utf-8
#################
# 习题15:读取文件
#################
# 前言
#
# 学习：如何读取本地文件（ex15_sample.txt）
# 

from sys import argv

#script, filename = argv
#VS下无法带参数调试
filename = "ex15_sample.txt"

txt = open(filename) #读写模式:r只读,r+读写,w新建(会覆盖原有文件),a追加,b二进制文件.常用模式

print "Here's your file %r:" % filename
print txt.read()
# txt.close()#处理完文件后将他关闭
# print txt.read()#测试是否关闭了


print "Type the  filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# 笔记
#
# 两种方法读取文件
# 1.得到文件名称——两种方法得到文件名
# 2.open（）打开文件
# 3.read（）输出文件
