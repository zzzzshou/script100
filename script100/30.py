"""
发送加密，返回要解密
AES CBC pack7 output base64
key=iv=55b3b62613aef1a0

解密 AES CBC packs7
key=iv=0a1fea31626b3b55
webpack的

"""
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


def test():
    timestamp = str(int(time.time() * 1000))
    url = 'https://www.maomaozu.com/index/hotlist.json'
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': '*/*',
    }
    model = AES.MODE_CBC
    key = '55b3b62613aef1a0'
    iv = '0a1fea31626b3b55'
    aes = AES.new(str(key).encode('UTF-8'), model, str(key).encode('UTF-8'))
    data = json.dumps(dict(expire=timestamp))
    data = aes.encrypt(pad(data.encode('UTF-8'), BLOCK_SIZE))
    data = base64.encodebytes(data)
    data = data.decode('UTF-8')
    data = data.strip()
    response = requests.request("POST", url, data=data, headers=headers)
    res = response.text
    print(res)


if __name__ == '__main__':
    test()
