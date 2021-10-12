'''

function toMD5Str(s) {
	var salt = "1#2$3%4(5)6@7!poeeww$3%4(5)djjkkldss";
	return hex_md5(s + "{" + salt + "}");
'''

import json
import random
import re

import requests
import hashlib
import urllib.parse
import time

import requests


def login(username, password):
    url = 'http://www.csti.cn/uc/login/servicelogin.do?method=login'
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',

    }
    mpassword = hashlib.md5(str(password + '{1#2$3%4(5)6@7!poeeww$3%4(5)djjkkldss}').encode('UTF-8')).hexdigest()

    data = 'account=' + username + '&pwd=' + mpassword + '&verify_code=&hid_remember_me=0&hid_remember_login_state=0&password=' + mpassword
    response = requests.request("POST", url, headers=headers, data=data)
    res = response.text
    print(res)


if __name__=='__main__':
    login()