# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:11:17 2021

@author: user
"""
#!pip install pycryptodome
from Crypto.Cipher import Salsa20
import random
import nltk
nltk.download('words')
from nltk.corpus import words

cipher_text1 = b'1v-\xdda\x9d\x13\xf5y\xd4M\xcc\xc2\xd5\xc9\xe8\xca\xfcF\xe1\x7f\xdd\xabM,=c\xa6\x9e\xd2M\x11;9Bpna\x91\xb8\xf5z>\x0cZ\x83\x11\xa7\x01\x1b\xc2\xc5$>\x10\xa2>"#\xc0\x98\xa4\xc2\xbd\xa1\xce\x0f\x17]\x8c_\xee\xadT|'
cipher_text2 = b'\x9d\x131v-\xdda\xe9\xf3,\xca\x02\xd1\xc9\x9a\xda\xe1\xce\xfcM\xed1\xdb\xb9\r,\x1b-\xa6\x88\x84JTo7N>p}\x9b\xfb\xa6e?\x0bQ\xc6_\xa7\x1d\x1a\x87\x8c78\x1a\xa9\x7f!!\xce\xdd\xe9\xd6\xbd\xf5\x9a\t\x17G\xc9K\xf2\xecDl\xb0\xca\x86\xa6\xd7\xde\xe5zxf\xd0\xado\xea'
cipher_text3 = b"\x00\x04\x00\x00\x00\x00\xfd7\xc1\x02\xcf\xc9\x82\xc4\xe1\xc7\xf1D\xef\x7f\xdd\xab\x10,\x00,\xea\x9d\xc1IC!qJ1ma\x9b\xba\xe7f>\x01N\x83\x0b\xa7\x0c\t\xde\xc537\x1b\xfby='\xca\x89\xe8\xda\xee\xf3\xdf\x14\x06V\xc5[\xf5\xadOj\xa9\xc1\x86\xb4\xdd\x8d\xff}|f\xd2\xado\xe6r\xf6\xcf\xe3\xf1H\xa6\xdaA\xcb\x17"
secret = 314159265358979323
key = secret.to_bytes(32, byteorder='big')
print("Key length in bytes", len(key))

unbroken_msg = []
ctext_nonce1 = cipher_text1[:8]
ciphertext1 = cipher_text1[8:]
cipher = Salsa20.new(key, nonce=ctext_nonce1)
dtext1 = cipher.decrypt(ciphertext1)
unbroken_msg.append(dtext1.decode('UTF-8',errors='ignore'))
ctext_nonce2 = cipher_text2[:8]
ciphertext2 = cipher_text2[8:]
cipher = Salsa20.new(key, nonce=ctext_nonce2)
dtext2 = cipher.decrypt(ciphertext2)
unbroken_msg.append(dtext2.decode('UTF-8',errors='ignore'))
ctext_nonce3 = cipher_text3[:8]
ciphertext3 = cipher_text3[8:]
cipher = Salsa20.new(key, nonce=ctext_nonce3)
dtext3 = cipher.decrypt(ciphertext3)
unbroken_msg.append(dtext3.decode('UTF-8',errors='ignore'))
print("nonce: ", ctext_nonce2)
print("Unbroken message: ", unbroken_msg[1])
message1 = []
for i in range(8):
    ciphertext = cipher_text1[i:]
    cipher = Salsa20.new(key, nonce=ctext_nonce2)
    dtext = cipher.decrypt(ciphertext)
    message1.append(dtext.decode('UTF-8',errors='ignore'))
message3 = []
for i in range(8):
    ciphertext = cipher_text3[i:]
    cipher = Salsa20.new(key, nonce=ctext_nonce2)
    dtext = cipher.decrypt(ciphertext)
    message3.append(dtext.decode('UTF-8',errors='ignore'))
for i in range(len(message1)):
    temp = message1[i].split()
    if temp[0].lower() in words.words():
        print("\nPlain text 1: ", message1[i])
print("Plain text 2: ", unbroken_msg[1])
for i in range(len(message3)):
    temp = message3[i].split()
    if temp[0].lower() in words.words():
        print("Plain text 3: ", message3[i])

