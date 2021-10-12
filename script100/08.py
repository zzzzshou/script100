'''
这个是个比较好玩的站


'''
import base64
import os
import random

import requests
import hashlib
import urllib.parse
import time


def login(username, password):
    code = ''
    url = "https://v4.passport.sohu.com/i/login/116005"
    mpassword = hashlib.md5(str(password+'1#2$3%4(5)6@7!poeeww$3%4(5)djjkkldss').encode('utf-8')).hexdigest()
    timestamp = int(round(time.time() * 1000))
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'cookie': ''
    }
    phone = str(username).encode('UTF-8')
    payload = 'userName=' + str(base64.b64encode(
        phone)) + '&struts.token.name=token&token=DX1W5ND8452LVYX23LI7ZG0AEHBU4C4B&password=' + mpassword + '&verifyCode=' + code
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.text
    print(res)


def Get_pic():
    url = "http://zzxt.hee.gov.cn/verifycode.do?width=70&height=20&codecount=4&codestyle=digit"
    response = requests.request("GET", url, )
    res = response.content
    cookie = response.cookies
    type = 1
    img_path = os.path.abspath('...') + '\\' + '{}.jpg'.format(type)
    with open(img_path, 'wb') as f:
        f.write(res)
    return res, cookie



if __name__=='__main__':
    Get_pic()