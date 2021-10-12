'''
本以为网易云的会挺难的。
            var bKf7Y = window.asrsea(JSON.stringify(i7b), bva4e(["流泪", "强"]), bva4e(Tu9l.md), bva4e(["爱心", "女孩", "惊恐", "大笑"]))
            {"csrf_token":"3ce787fc790486f0ecc4e5c62f8bef70"}两次AES，第一次的key是bva4e(["爱心", "女孩", "惊恐", "大笑"]，第二次是随机的。
AES加密。key是随机的

    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    iv=0102030405060708
    然后还有一个RSA加密顺手也解决了
    公钥00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
    模数=010001

    encSecKey=RSA加密key

思路就到这里了，没什么难度

'''