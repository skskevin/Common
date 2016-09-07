#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-07 12:36:51
# @Author  : dongchuan
# @Version : 1.0
# @Desc : 测试
import binascii
from common import *
from Crypto.Cipher import AES

id = 48
key = md5('ffan_@%sec^&_team)(')
data = baseN(id, 36)


ciphertext = encrypt(data, key, AES.MODE_ECB)
print binascii.b2a_hex(ciphertext)
