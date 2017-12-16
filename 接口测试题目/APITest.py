# coding=utf8

import requests,json
def addMessage(school_uid,bookmark_uid):
    payoad = {
        'school_uid':school_uid,
        'bookmark_uid':bookmark_uid,
        'action': 'add'
    }
    param = {'Cookie': 'passport=8dc31981dc397bbbdb85a087ea2a8e704b717d92'}
    reponses = requests.post('http://ai.seewo.com/api/repository/bookmark/school/', headers=param, data=payoad)
    bodyDict = reponses.json()
    # print json.dumps(bodyDict,indent=2).decode("unicode-escape")

    if bodyDict["code"] == 0:
        print '输入的school_uid：%s，输入的bookmark_uid：%s；信息增加成功' %(school_uid,bookmark_uid)
    else:
        print '输入的school_uid：%s，输入的bookmark_uid：%s；信息增加失败' %(school_uid,bookmark_uid)


def listTest():
    testList = []
    param = {'Cookie': 'passport=8dc31981dc397bbbdb85a087ea2a8e704b717d92'}
    response = requests.get('http://ai.seewo.com/api/exam/list', headers=param)
    r = response.json()
    # print json.dumps(r,indent=2).decode("unicode-escape")

    dataList = r["data"]
    for one in dataList:
        name = one["name"]
        testList.append(name)
    lenList = len(testList)
    return lenList,testList





