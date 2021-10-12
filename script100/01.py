"""

bv的值为UA 直接取MD5
UA固定，bv也可以固定
故此示例中bv固定即可

"""

import random

import requests
import hashlib
import urllib.parse
import time


def tanslation(words):
    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
        'cookie': '',

    }
    timestamp = int(round(time.time() * 1000))
    salt = str(timestamp) + str(random.randint(0, 9))
    sign = hashlib.md5(str('fanyideskweb' + words + salt + 'Y2FYu%TNSbMCxc3t2u^XT').encode('utf-8')).hexdigest()
    data = 'i=' + urllib.parse.quote(words) + '&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt' \
                                              '=' + salt + '&sign' \
                                                           '=' + sign + '&lts=' + str(
        timestamp) + '&bv=36756d23dc251cc14bf9558b9730e3a5&doctype=json' \
                     '&version=2.1&keyfrom=fanyi.web&action=FY_BY_REALTlME '
    response = requests.request("POST", url, data=data, headers=headers)
    res = response.text
    print(res)


if __name__ == '__main__':
    tanslation('马赛克')
