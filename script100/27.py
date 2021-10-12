"""
返回值解密的例子

’eyJpdiI6Ik83S2JUN3NlZ1orWXpRVVBmT1NKZkE9PSIsInZhbHVlIjoiNWQ4RWlDSUx2Vlk3RlwvbWthd2FIc3hNcEN3NjNTY3lYdHFudlM1dG8wM0k9IiwibWFjIjoiZWY3NWRhYzRjYzgwN2RlMDFiNmViOGVjYjJhN2ZlOTI2OTQ0Y2MwMjVmMTFiMWNjZGJjNzlkNmQ3NjBkNGY5ZiJ9‘
原文

"""
import base64
import json
import random
import requests
import hashlib
import urllib.parse
import time
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
import execjs


def js_from_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()

    return result


text = 'eyJpdiI6Ik83S2JUN3NlZ1orWXpRVVBmT1NKZkE9PSIsInZhbHVlIjoiNWQ4RWlDSUx2Vlk3RlwvbWthd2FIc3hNcEN3NjNTY3lYdHFudlM1dG8wM0k9IiwibWFjIjoiZWY3NWRhYzRjYzgwN2RlMDFiNmViOGVjYjJhN2ZlOTI2OTQ0Y2MwMjVmMTFiMWNjZGJjNzlkNmQ3NjBkNGY5ZiJ9'.encode(
    'UTF-8')
text = base64.b64decode(text)
print(text)
json_data = json.loads(text)
key = 'UVJgCE+OFIff3hK5BT5sPBbGZzjR6FwntjSCwOA9tUQ='
iv = json_data['iv']
value = json_data['value']
print(iv)
context1 = execjs.compile(js_from_file('27.js'))
res = context1.call("AES_Decrypt", value, iv)
print(res)
