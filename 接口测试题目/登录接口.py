# coding=utf8

import requests,json

payload = {
    'username':'13012341235',
    'password':'123456'
}
response = requests.post("http://ai.seewo.com/api/user/login",data=payload)
print response.cookies['passport']
bodyDict = response.json()
print json.dumps(bodyDict,indent=2).decode("unicode-escape")




