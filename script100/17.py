import base64
import random
import requests
import hashlib
import time

'''
这个还行。salt是动态的了
login_md5(pwd, datetime_num) { return hex_md5("@345Kie(873_dfbKe>d3<.d23432="+hex_md5("EW234@![#$&]*{,OP}Kd^w349Op+-32_" + pwd + datetime_num)); }
'''


def login(username, password):
    timestamp = str(int(time.time()))
    mpassword = hashlib.md5(str('EW234@![#$&]*{,OP}Kd^w349Op+-32_'+password+timestamp).encode('UTF-8')).hexdigest()
    mpassword = hashlib.md5(str('@345Kie(873_dfbKe>d3<.d23432='+mpassword).encode('UTF-8')).hexdigest()
    url = 'https://u.faloo.com/regist/Login.aspx?txtUserID='+username+'&txtPwd='+mpassword+'&txtPwd4temp=&verifyCode=EHEW&ts='+timestamp+'&t=2&GJ630531=1011&backurl=https%3A%2F%2Fb.faloo.com92F'
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

    }

    response = requests.request("GET", url, headers=headers)
    res = response.text
    print(res)
