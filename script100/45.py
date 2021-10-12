import base64
import json
import random
import requests
import hashlib
import urllib.parse
import time
from Cryptodome.Util.Padding import pad
import execjs


def js_from_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()

    return result


def login(username, password):
    context = execjs.compile(js_from_file('/44.js'))
    password = context.call('encrypt', password)
    url = 'https://passport.fang.com/login.api'
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 '
                      'Safari/537.36',
        'Accept': '*/*',
    }
    password = base64.b64decode(password).hex()#base64tohex
    #hextob64
    '''
    hex_str='c2889d8f'
    result2 = b2a_base64(bytes.fromhex(hex_str))
    print('result2:',result2) # result2: b'woidjw==\n'
    '''
    data = 'uid=' + username + '&pwd=' + password + '&Service=soufun-passport-web&AutoLogin=1'
    response = requests.request("POST", url, data=data, headers=headers)
    res = response.text
    print(res)
