"""
本来是搞登陆的算法的，后来发现没有账号，注册的时候发现有滑块和文字点选。
风控大概是滑块次数
滑块唤起3次左右就会变成文字点选。
加密算法一样的。
RSA加密。
密钥为
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCj+WG/EdwJXcaINIlSyrHjeLmZsk7C9NnkqzrOJ2uYG7M2QSaLVygtlftSDQ8ccC3KsYaS9gnVPlWggJf9h49tDW/vCnlnYehcLwVDtmSGHON/wyZfmLgARbjHxcmxEifmLJAKf+Vg3zqwk05jRa9occxTY3HsPjVYdQWL83DTiQIDAQAB
点选的明文为'passport{"data":{"r1":"186|122|1633853250319","r2":"79|161|1633853250756",这里就不给全了

"""

import random
import requests
import hashlib
import urllib.parse
import time

import requests


def login(username, password):
    url = "https://v4.passport.sohu.com/i/login/116005"
    mpassword = hashlib.md5(str(password).encode('utf-8')).hexdigest()
    timestamp = int(round(time.time() * 1000))
    headers = {
        'Host': 'v4.passport.sohu.com',
        'Connection': 'keep-alive',
        'Content-Length': '110',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://www.sohu.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'iframe',
        'Referer': 'https://www.sohu.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': ''
    }
    payload = 'userid=' + username + '&password=' + mpassword + '&appid=116005&callback=passport403_cb' + str(timestamp)
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.text
    print(res)


if __name__ == '__main__':
    '''
    需要自己填充cookie
    '''
    username = ''
    password = ''
    login(username, password)
'''
<script>
    document.domain = "sohu.com";
    parent.passport403_cb1633854611380({"body":"","message":"Success","status":200});
</script>

'''
