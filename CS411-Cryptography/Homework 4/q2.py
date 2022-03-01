# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:15:30 2021

@author: user
"""

from RSA_OAEP import *
import math
import timeit
import random
import sympy
import warnings
import requests
from Crypto.Hash import SHA3_256
from Crypto.Hash import SHA3_384
from Crypto.Hash import SHA3_512
from Crypto.Hash import SHAKE128, SHAKE256

API_URL = 'http://cryptlygos.pythonanywhere.com'

my_id = 25331   ## Change this to your ID number

def RSA_OAEP_Get():
  response = requests.get('{}/{}/{}'.format(API_URL, "RSA_OAEP", my_id )) 	
  c, N, e = 0,0,0 
  if response.ok:	
    res = response.json()
    print(res)
    return res['c'], res['N'], res['e']
  else:
    print(response.json())
    return c, N, e

def RSA_OAEP_Checker(PIN_):
  # Client sends PIN_
  response = requests.put('{}/{}/{}/{}'.format(API_URL, "RSA_OAEP", my_id, PIN_))
  print(response.json())

#get the parameters
c, N, e = RSA_OAEP_Get()

# #Calculate the PIN_ and check your answer
# RSA_OAEP_Checker(PIN_)

myflag = True
for m in range(1000, 10000):
    if (myflag):
        for R in range(2**(k0-1), 2**k0):
            c_ = RSA_OAEP_Enc(m, e, N, R)
            if c == c_:
                print("You have found the PIN = {} with the following R = {}.".format(m, R))
                myflag = False
                PIN = m
                break
    else:
            break        
RSA_OAEP_Checker(PIN)        
        
        
        
        