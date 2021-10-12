'''
简单的AES


'''
import base64
import json
import random
import requests
import hashlib
import urllib.parse
import time
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

BLOCK_SIZE = 32


def login(username, password):
    url = 'https://www.dns.com/login'
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': '*/*',
    }
    # _token值由'https://www.dns.com/member'get一下即可
    model = AES.MODE_CBC
    key = '1234567890abcDEF'
    aes = AES.new(str(key).encode('UTF-8'), model, str(key).encode('UTF-8'))
    password = aes.encrypt(pad(password.encode('UTF-8'), BLOCK_SIZE))
    password = base64.encodebytes(password)
    password = password.decode('UTF-8')
    password = password.strip()
    username = aes.encrypt(pad(username.encode('UTF-8'), BLOCK_SIZE))
    username = base64.encodebytes(username)
    username = username.decode('UTF-8')
    username = username.strip()

    data = '_token=&password=' + urllib.parse.quote(password) + '&email=' + urllib.parse.quote(
        username) + '&redirectTo=https%3A%2F%2Fwww.dns.com%2Fdashboard'
    response = requests.request("POST", url, data=data, headers=headers)
    res = response.text
    print(res)
