#coding:utf-8
#################
# 习题11:提问
#################
# 前言
#
# 这里主要理解：接收用户的输入
#

print "How old are you?",
# 接收控制台的输入信息
age = raw_input() # 在python3.x 中，raw_input 被 input代替（待深究）
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So,you're %s old, %s tall and %s heavy." % (age, height, weight)
	
# 笔记	
# 1.raw_input()是接受控制台输入的任何信息
# 2.在print后面加“,”可以让输入在同一行

