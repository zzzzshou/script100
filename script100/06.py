import json
import os
import random
import re
import requests
import hashlib
import urllib.parse
import time
import requests
import execjs


def login(username, password):
    url = 'http://rrwapi.renren.com/account/v1/loginByPassword'
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    }
    timestamp = str(int(round(time.time() * 1000)))
    mpassword = hashlib.md5(str(password).encode('UTF-8')).hexdigest()
    sign = hashlib.md5(
        str('appKey=bcceb522717c2c49f895b561fa913d10callId=' + timestamp + 'password=' + mpassword + 'sessionKey=user=' + username + 'bcceb522717c2c49f895b561fa913d10').encode(
            'UTF-8')).hexdigest()
    data = json.dumps(dict(user=username, password=mpassword, appKey='bcceb522717c2c49f895b561fa913d10', sessionKey='',
                           callId=timestamp, sig=sign))
    response = requests.request("POST", url, headers=headers, data=data)
    res = response.text
    print(res)


if __name__ == '__main__':
    username = ''
    password = ''
    login(username, password)
