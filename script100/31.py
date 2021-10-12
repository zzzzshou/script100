'''

简单
电信的页面相当的卡。卡的难受，也没有发现调试会造成内存变大的代码QAQ
应该就是web端做的不太好
AES较哈希系列稍微难一点点。
应该是用的最多的算法
其次就是RSA了

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




def login(username, password):
    url = 'https://login.189.cn/web/login'
    model = AES.MODE_CBC
    key = '33b21adee1b8620a7ba81aea1a80c724'
    iv = '1234567812345678'
    aes = AES.new(str(key).encode('UTF-8'), model, str(key).encode('UTF-8'))
    password = aes.encrypt(pad(password.encode('UTF-8'), BLOCK_SIZE))
    password = base64.encodebytes(password)
    password = password.decode('UTF-8')
    password = password.strip()
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': '*/*',
    }
    data = 'Account=' + username + '&UType=201&ProvinceID=12&AreaCode=&CityNo=&Captcha=PPQK&RandomFlag=0&Password=' + urllib.parse.quote(
        password)
    response = requests.request("POST", url, data=data, headers=headers)
    res = response.text
    print(res)


# 懒死了，现在才写这玩意。
def AES_Encrypt(key, iv, data):
    BLOCK_SIZE = 32
    model = AES.MODE_CBC
    aes = AES.new(str(key).encode('UTF-8'), model, str(iv).encode('UTF-8'))
    data = aes.encrypt(pad(data.encode('UTF-8'), BLOCK_SIZE))
    data = base64.encodebytes(data)
    data = data.decode('UTF-8')
    data = data.strip()
    return data
