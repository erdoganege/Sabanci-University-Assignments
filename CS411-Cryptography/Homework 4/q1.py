# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:56:03 2021

@author: user
"""
import math
import random
import warnings
import sympy

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    if a < 0:
        a = m+a
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
import random
import requests
from random import randint

API_URL = 'http://cryptlygos.pythonanywhere.com'

my_id = 25331   #Change this to your ID


def RSA_Oracle_Get():
  response = requests.get('{}/{}/{}'.format(API_URL, "RSA_Oracle", my_id)) 	
  c, N, e = 0,0,0 
  if response.ok:	
    res = response.json()
    print(res)
    return res['c'], res['N'], res['e']
  else:
    print(response.json())

def RSA_Oracle_Query(c_):
  response = requests.get('{}/{}/{}/{}'.format(API_URL, "RSA_Oracle_Query", my_id, c_)) 
  print(response.json())
  m_= ""
  if response.ok:	m_ = (response.json()['m_'])
  else: print(response)
  return m_

def RSA_Oracle_Checker(m):
  response = requests.put('{}/{}/{}/{}'.format(API_URL, "RSA_Oracle_Checker", my_id, m))
  print(response.json())

#get the parameters
c, N, e = RSA_Oracle_Get()
# #choose a ciphertext and get the corresponding plaintext
# m_ = RSA_Oracle_Query(c_)   
# #Calculte m using m_
# RSA_Oracle_Checker(m) #m should be string
temp = 5
temp_inv = modinv(temp, N)
c_ = (pow(temp,e,N)*c)%N
m_ = RSA_Oracle_Query(c_)   
m = (m_ * temp_inv) % N
print("My message is following:", m.to_bytes((m.bit_length() + 7) // 8, byteorder='big'))
RSA_Oracle_Checker(m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode("UTF-8"))













