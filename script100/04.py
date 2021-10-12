import json
import os
import random
import re
import requests
import hashlib
import urllib.parse
import time
import requests
import execjs

'''
这里，不放识别库了。手动识别之后提交结果+cookie来过校验
main里面分两步
这个的md5里面处理了一下下。扣了JS直接调用。

'''


def Get_ticker():
    timestamp = str(int(round(time.time() * 1000)))
    url = 'https://checkcode.99.com/token?action=getticket&bussiness=aq_login&callback=&_=' + timestamp
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 '
                      'Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    }
    response = requests.request("GET", url, headers=headers)
    res = response.text
    print(res)
    try:
        json_data = json.loads(res)
        ticket = json_data['ticket']
        return ticket
    except Exception as e:
        print(e)
        pass


def Get_piccode(ticket):
    timestamp = str(int(round(time.time() * 1000)))
    url = 'https://aq.99.com/AjaxAction/AC_verifycode.ashx?CallBack=&nduseraction=getverifycodestate&verifycodetype' \
          '=UserLogin&bussiness=aq_login&ticket=' + ticket + '&SiteFlag=995&RND=0.7527175841267677&_=' + timestamp
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 '
                      'Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    }
    response = requests.request("GET", url, headers=headers)
    res = response.text
    print(res)
    try:
        json_data = json.loads(res)
        VerifyCodeUrl = json_data['VerifyCodeUrl']
        VerifyToken = json_data['VerifyToken']
        print(VerifyToken)
        return VerifyCodeUrl, VerifyToken
    except Exception as e:
        print(e)
        pass


def pic_download(url, type):
    img_path = os.path.abspath('...') + '\\' + '{}.jpg'.format(type)
    img_data = requests.get(url).content
    with open(img_path, 'wb') as f:
        f.write(img_data)
    print(img_path)
    return img_path


def js_from_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()

    return result


def login(username, password, code):
    timestamp = str(int(round(time.time() * 1000)))
    context1 = execjs.compile(js_from_file('/04.js'))

    mpassword = context1.call("getMD5Value", password)

    url = 'https://aq.99.com/AjaxAction/AC_userlogin.ashx?CallBack=&siteflag=995&nduseraction=login&txtUserName=' + username + '&txtPassword=' + mpassword + '&checkcode=' + code + '&Rnd=0.092623166489048&aws=371f7c2ba2c09affbc4977afc763b49c&_=' + timestamp
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 '
                      'Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
        'cookie': 'UserCookie=' + VerifyToken
    }
    response = requests.request("GET", url, headers=headers)
    res = response.text
    print(res)


if __name__ == '__main__':
    ticket = Get_ticker()
    VerifyCodeUrl, VerifyToken = Get_piccode(ticket)
    pic_download(VerifyCodeUrl, 1)
    # 手动填写cookie
    login('', '', '')
