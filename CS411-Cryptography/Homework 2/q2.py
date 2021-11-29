# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 14:37:40 2021

@author: user
"""
import random
import requests
import math
import warnings
import sympy
#API_URL = 'http://10.36.52.109:6000'
API_URL = 'http://cryptlygos.pythonanywhere.com'
my_id = 25331   
def getQ2():
  endpoint = '{}/{}/{}'.format(API_URL, "Q2", my_id )
  response = requests.get(endpoint) 	
  if response.ok:	
    res = response.json()
    e, cipher = res['e'], res['cipher']
    return e, cipher
  else:  print(response.json())
def checkQ2(ptext):  #check your answer for Question 1 part c
  response = requests.put('{}/{}'.format(API_URL, "checkQ2"), json = {"ID": my_id, "msg":ptext})
  print(response.json()) 
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m   
p = 23736540918088479407817876031701066644301064882958875296167214819014438374011661672830210955539507252066999384067356159056835877781419479023313149139444707
q = 62179896404564992443617709894241054520624355558658288422696178839274611833136662241430162694076231401545584449128278988404970580015985140542451087049794069
e, cipher = getQ2()
print("Returned values of e: {}\ncipher: {}".format(e,cipher))
n = p * q
phi_n = (p-1) * (q-1)
d = modinv(e, phi_n)
m = pow(cipher, d, n)
print("Our phi of n is: {}\nOur d is: {}\nOur m is: {}".format(phi_n, d, m))
# total_length = (m.bit_length() // 8) + 1
my_bytes = m.to_bytes(m.bit_length(), byteorder='big')
my_bytes = my_bytes.lstrip(b'\x00')
text = my_bytes.decode('utf-8')
print("Our text is: {}".format(text))
checkQ2(text)


