"""
password明文为随机64位字符+密码
key是get登陆接口获取的salt
iv是随机的16位
迷惑行为
我没找到传输IV的地方，不知道服务器是怎么样校验的IV
经过实验发现不校验IV。随便传IV即可解密。。
到底还是不安全

"""