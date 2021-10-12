import base64
import json
import random
import requests
import hashlib
import urllib.parse
import time
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

'''
aes模块用起来不顺手
调用JS吧

'''
BLOCK_SIZE = 32
import execjs


def js_from_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()

    return result


def login(username, password):
    timestamp = str(int(time.time() * 1000))
    sign = hashlib.md5(str(timestamp + 'bdc739ff2dcf').encode('UTF-8')).hexdigest().upper()
    url = 'https://gateway.ewt360.com/api/authcenter/v2/oauth/login/account'

    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': '*/*',
        'timestamp': timestamp,
        'sign': sign
    }
    context = execjs.compile(js_from_file('28.js'))
    password = context.call('AES_Encrypt', password)
    password = password.upper()
    data = json.dumps(dict(platform=1, userName=username, password=password, autoLogin='true'))
    response = requests.request("POST", url, data=data, headers=headers)
    res = response.text
    print(res)
