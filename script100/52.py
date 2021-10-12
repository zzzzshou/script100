'''


function jsEncrypt(word) {
    var pubKey = '-----BEGIN PUBLIC KEY-----\n' +
        'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCnpF5Yds3y5xt4KjtThxh1FueD\n' +
        'T7UIbznhcR9F6aJbQp+TleyuAJWwPETl9MzZBjObKTGmWXIufaIZlaENG0gIegy1\n' +
        'X/NgjsVBtVNZZ3HVpfNsiGCUIDkvm3UtrVoSG8IBbm3in+i9DeqLdXdI6ip3YR35\n' +
        'vuOEYcQt8v/+fr8iIwIDAQAB\n' +
        '-----END PUBLIC KEY-----\n';
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(pubKey);
    var encrypted = encrypt.encrypt(word);
    return encrypted;
}

直接就写出来了


'''