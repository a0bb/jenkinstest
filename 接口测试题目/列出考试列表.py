# coding=utf8

import requests,json
import APITest


name = APITest.listTest()[1]
total = APITest.listTest()[0]
#判断列表上是否符合预期
compareList = ['语文','数学']
if compareList == name:
    print "考试列表符合预期"
else:
    print '考试列表不符合预期'

#列表总数
print total

