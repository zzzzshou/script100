'''
没找到signature在那个包
           i = function() {
            var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {}
              , t = o.get("Authorization") || ""
              , r = Math.random().toString(36).slice(-6)
              , i = Date.parse(new Date) / 1e3
              , a = {
                nonce: r,
                timestamp: i,
                signature: n.SHA256("".concat(t).concat(r).concat(i, "zfm9p4vDti6N4xyIsEamjzFjpUfC7G3r")).toString()
            }

加密点找到了倒是
7ece94d9f9c202b0d2ec557dg4r9bc
'''
import json
import random
import requests
import hashlib
import urllib.parse
import time


def translation(words):
    sign = hashlib.md5(str('6key_cibaifanyicjbysdlove1'+words).encode('UTF-8')).hexdigest()
    sign = sign[0:16]
    url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=' + sign
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',

    }

    data = 'from=zh&to=en&q=' + urllib.parse.quote(words)
    response = requests.request("POST", url, data=data, headers=headers)
    res = response.text
    print(res)


if __name__ == '__main__':
    translation('利物浦')
