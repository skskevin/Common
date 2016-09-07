#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-07 12:36:51
# @Author  : dongchuan
# @Version : 1.0
# @Desc : 公共函数
import hashlib
import Padding
from Crypto.Cipher import AES


# MD5加密
def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


# 10进制转任意进制(1<b<37)
def baseN(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


# AES加解密
def encrypt(plaintext, key, mode):
    plaintext = Padding.appendPadding(plaintext, blocksize=Padding.AES_blocksize, mode=0)
    encobj = AES.new(key, mode)
    return(encobj.encrypt(plaintext))


def decrypt(ciphertext, key, mode):
    encobj = AES.new(key, mode)
    return(encobj.decrypt(ciphertext))
