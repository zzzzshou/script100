"""
https://a1.m1907.cn/api/v/?z=5d855143e6fd5d1a252ac6c34b2b7e0f&jx=%E5%93%88%E5%88%A9%C2%B7%E6%B3%A2%E7%89%B9%E4%B8%8E%E5%AF%86%E5%AE&s1ig=11397&g=
m1907站m3u8下载
这里只讨论Z参数生成

"""
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


def test():
    x = '22'
    x1 = hashlib.md5(x.encode('UTF-8')).hexdigest()
    x2 = x1[0:10]
    z = hashlib.md5(x2.encode('UTF-8')).hexdigest()
    print(z)


if __name__ == '__main__':
    test()
