"""
拉勾网
只写个登陆密码加密，其他的没什么意思。一个极验的无感验证
https://www.lgstatic.com/lg-passport-fed/static/pkg/pc/page/login/main.html_aio_0b5f898.js:formatted
        var c, g = b.collectData(), v = "veenike", F = g.password;
        g.password = md5(g.password),
        g.password = md5(v + g.password + v),
也是比较简单
写到现在差不多10个，基本上没有超过3分钟的。MD5的太简单了
拉勾的加密看上面抠出来的JS也可以看明白。
用python实现如下
header太长了，没什么要校验的。就写个加密实现好了
"""
import base64
import random
import requests
import hashlib
import time

password = ''
salt = 'veenike'
password = hashlib.md5(str(password).encode('UTF-8')).hexdigest()
password = hashlib.md5(str(salt+password+salt).encode('UTF-8')).hexdigest()
