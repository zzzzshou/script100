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
    password = context.call('getpwd', password)
    url = 'https://oauth.d.cn/auth/login?display=web&name=' + username + '&pwd=' + urllib.parse.quote(
        password) + '&to=https%253A%252F%252Fwww.d.cn%252F'
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 '
                      'Safari/537.36',
        'Accept': '*/*',
    }

    response = requests.request("GET", url, headers=headers)
    res = response.text
    print(res)
