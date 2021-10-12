import base64
import json
import random
import requests
import hashlib
import urllib.parse
import time
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
import execjs


def js_from_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()

    return result


def login(username, password):
    url = 'http://ptlogin.4399.com/ptlogin/login.do?v=1'
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 '
                      'Safari/537.36',
        'Accept': '*/*',
    }
    context = execjs.compile(js_from_file('41.js'))
    password = context.call('encryptAES', password)
    data = 'loginFrom=uframe&postLoginHandler=default&layoutSelfAdapting=true&externalLogin=qq&displayMode=popup' \
           '&layout=vertical&bizId=&appId=www_home&gameId=&css=&redirectUrl=&sessionId=&mainDivId=popup_login_div' \
           '&includeFcmInfo=false&level=0&regLevel=4&userNameLabel=4399%E7%94%A8%E6%88%B7%E5%90%8D&userNameTip=%E8%AF' \
           '%B7%E8%BE%93%E5%85%A54399%E7%94%A8%E6%88%B7%E5%90%8D&welcomeTip=%E6%AC%A2%E8%BF%8E%E5%9B%9E%E5%88%B04399' \
           '&sec=1&password=' + urllib.parse \
               .quote(password) + '&username=' + username + '&autoLogin=on'
    response = requests.request("POST", url, data=data, headers=headers)
    res = response.text
    print(res)
