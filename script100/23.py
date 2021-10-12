'''
挺简单的
'''
import json
import random
import requests
import hashlib
import urllib.parse
import time

import requests


def Get_nonce(username):
    url = 'https://www.doyo.cn/User/Passport/token?username=' + username + '&random=0.3505296732742438'
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    }
    response = requests.request("GET", url, headers=headers)
    res = response.text
    print(res)
    try:
        json_data = json.loads(res)
        nonce = json_data['nonce']
        ts = json_data['ts']
        return nonce, ts
    except Exception as e:
        print(e)
        pass


def login(username, password, nonce, ts):
    url = 'https://www.doyo.cn/User/Passport/login'
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    }
    # next参数是网址的URL编码之后base64编码，无视即可
    mpassword = hashlib.sha1(str(nonce + password + ts).encode('UTF-8')).hexdigest()

    data = 'username=' + username + '&password=' + mpassword + '&remberme=1&next=aHR0cHMlM0ElMkYlMkZ3d3cuZG95by5jbiUyRg%3D%3D'
    response = requests.request("GET", url, data=data, headers=headers)
    res = response.text
    print(res)


if __name__ == '__main__':
    username = ''
    password = ''
    nonce, ts = Get_nonce(username)
    login(username, password, nonce, ts)
