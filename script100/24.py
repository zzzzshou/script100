"""
黑猫投诉查询
function d(e, t, r) {
        var n = ""
          , i = t
          , a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
        e && (i = Math.round(Math.random() * (r - t)) + t);
        for (var o = 0; o < i; o++) {
            n += a[Math.round(Math.random() * (a.length - 1))]
        }
        return n
    }(!1, 16)
 l = "$d6eb7ff91ee257475%"

"""
import json
import random
import requests
import hashlib
import urllib.parse
import time


def test():
    couid = '6384912431'
    timestamp = str(int(time.time()) * 1000)
    rs = 'EZoEKxBufjjt9FQl'  # rs是JS生成的。
    sign = hashlib.sha256(str('$d6eb7ff91ee257475%1110' + timestamp + couid + rs).encode('UTF-8')).hexdigest()
    url = 'https://tousu.sina.com.cn/api/company/received_complaints?ts=' + timestamp + '&rs=' + rs + '&signature=' + sign + '&callback=&couid=' + couid + '&type=1&page_size=10&page=1&_=' + str(
        int(timestamp) - 20)
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
        'cookies': 'UOR=www.baidu.com,mail.sina.com.cn,; SINAGLOBAL=223.98.104.123_1617637974.771719; '
                   'SGUID=1618520450694_65857631; '
                   '__gads=ID=75c74a2f94842f43-226cc20268c70072:T=1618520506:RT=1618520506:S'
                   '=ALNI_MaHf8pcTTWNky_zWp3Qzb6L5d0FjA; U_TRS1=0000007b.8b5e1f7d.6078aa75.1be6406f; TOUSU-SINA-CN=; '
                   'UM_distinctid=17c6ddbd965234-0ad51f2d8e5031-b7a1438-1fa400-17c6ddbd9661e5; '
                   'CNZZDATA1273941306=919078403-1633929663-%7C1633929663; Apache=111.22.249.154_1633930697.154666; '
                   'ULV=1633930713893:6:2:2:111.22.249.154_1633930697.154666:1633930696921 '
    }
    response = requests.request("GET", url, headers=headers)
    res = response.text
    print(res)


if __name__ == '__main__':
    test()
