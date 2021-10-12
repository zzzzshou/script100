import json
import random
import re

import requests
import hashlib
import urllib.parse
import time

import requests


def login(username, password, cookie, keytime):
    url = 'http://qpbjs.91hylbc.com/ajax/login.ashx?action=login'
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
        'cookie': cookie,

    }
    timestamp = str(int(round(time.time() * 1000)))

    sign = hashlib.md5(str('keytime=' + keytime + '&password=' + password + '&time=' + str(
        timestamp) + '&username=' + username + '03630BCA9381270FCD2F695AE76E2660').encode('UTF-8')).hexdigest()
    sign = sign.upper()
    data = json.dumps(dict(username=username, password=password, time=timestamp, keytime=keytime, sign=sign))
    response = requests.request("POST", url, headers=headers, data=data)
    res = response.text
    print(res)


def Get_cookies():
    url = 'http://qpbjs.91hylbc.com/Login.aspx?pageurl=/UserCenter/Center.aspx'
    response = requests.request("GET", url, )
    res = response.text
    pattern = re.compile('([a-f\d]{32}|[A-F\d]{32})')
    key = pattern.search(res)
    keytime = key.group(1)
    ck = response.cookies
    pattern = re.compile('Cookie (.*?) for qpbjs.91hylbc.com')
    cookie = pattern.search(str(ck)).group(1)
    return keytime, cookie


if __name__ == '__main__':
    username = '18884414451'
    password = 'qwer1234'
    keytime, cookie = Get_cookies()
    login(username, password, cookie, keytime)
