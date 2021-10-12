'''
图片里面的链接不全。不过访问看到熟悉的月球见，我就知道是mytoken的。之前做过
算法也比较简单
简单还原一下吧


'''
import base64
import random
import requests
import hashlib
import time

timestamp = str(int(time.time() * 1000))
salt = timestamp[0:6]
sign = hashlib.md5(str(timestamp+'9527'+salt).encode('UTF-8')).hexdigest()