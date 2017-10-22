# coding=utf8

import requests,json

testList = []
param = {'Cookie':'passport=8dc31981dc397bbbdb85a087ea2a8e704b717d92'}

response = requests.get('http://ai.seewo.com/api/exam/list',headers=param)
r = response.json()

#print json.dumps(r,indent=2).decode("unicode-escape")

dataList=r["data"]
for one in dataList:
    name = one["name"]
    testList.append(name)

#判断列表上是否符合预期
compareList = ['语文','数学']
if compareList == testList:
    print "考试列表符合预期"
else:
    print '考试列表不符合预期'

#列表总数
lenList = len(testList)
print '考试列表一共有：%d' %lenList

