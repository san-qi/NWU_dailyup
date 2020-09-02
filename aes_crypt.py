from Crypto.Cipher import AES
import base64


class AesCrypt:
    BLOCK_SIZE = 16

    def __init__(self, _key, _iv):
        self.key = _key.encode('utf8')
        self.iv = _iv.encode('utf8')

    @staticmethod
    def pad(s):
        pad_len = AesCrypt.BLOCK_SIZE - len(s) % AesCrypt.BLOCK_SIZE
        return s + pad_len * chr(pad_len)

    @staticmethod
    def un_pad(s):
        return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, data):
        # 加密
        # 字符串补位
        data = self.pad(data)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
        encrypted_bytes = cipher.encrypt(data.encode('utf8'))
        # 对byte字符串按utf-8进行解码
        encode_str = base64.b64encode(encrypted_bytes)
        return encode_str.decode('utf8')

    def decrypt(self, data):
        # 解密
        data = data.encode('utf8')
        encode_bytes = base64.decodebytes(data)
        # 将加密数据转换位bytes类型数据
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        text_decrypted = cipher.decrypt(encode_bytes)
        # 去补位
        text_decrypted = self.un_pad(text_decrypted)
        text_decrypted = text_decrypted.decode('utf8')
        return text_decrypted


class MyAes(AesCrypt):
    random_str = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'
    from random import random

    def __init__(self, _key):
        _iv = ''
        for _ in range(16):
            _iv += MyAes.random_str[int(self.random()*len(MyAes.random_str))]
        AesCrypt.__init__(self, _key, _iv)

    def encrypt(self, data):
        pad_str = ''
        for _ in range(64):
            pad_str += MyAes.random_str[int(self.random()*len(MyAes.random_str))]
        return AesCrypt.encrypt(self, pad_str + data)


if __name__ == '__main__':
    key = 'JSc1Y5biui3UCpBZ'
    iv = '1234567890123456'
    pw = 'Zyx131417'
    text = 'WqFoUlfP5gxD5Tp0jSYxx6rQuw1b4FD9tjgVKMaaMKYZpMEkFvoC/RAQS3q5SWV0Fqyso2B5kRey+Sz0CqwSa0x66slgrmJ6zXEQ4NfttdM='

    t = MyAes(key)
    e = t.encrypt(pw)  # 加密
    print("加密:", e)
    print("加密:", text)
    d = t.decrypt(e)  # 解密
    print("解密:", d)
