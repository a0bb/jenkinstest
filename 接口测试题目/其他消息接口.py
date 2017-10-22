# coding=utf8

import requests,json

payoad={
    'school_uid':'2f0f6935',
    'bookmark_uid':'ed6686a',
    'action':'add'
}
param = {'Cookie':'passport=8dc31981dc397bbbdb85a087ea2a8e704b717d92'}
reponses = requests.post('http://ai.seewo.com/api/repository/bookmark/school/',headers=param,data=payoad)
bodyDict = reponses.json()
#print json.dumps(bodyDict,indent=2).decode("unicode-escape")

if bodyDict["code"] == 0:
    print '信息增加成功'
else:
    print '信息增加失败'