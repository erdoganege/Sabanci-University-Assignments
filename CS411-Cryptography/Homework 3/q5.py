# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 21:20:27 2021

@author: user
"""

import random
import requests
from BitVector import *

API_URL = 'http://cryptlygos.pythonanywhere.com'
my_id = 25331   

def get_poly():
  endpoint = '{}/{}/{}'.format(API_URL, "poly", my_id )
  response = requests.get(endpoint) 	
  a = 0
  b = 0
  if response.ok:	
    res = response.json()
    print(res)
    return res['a'], res['b']
  else:
    print(response.json())

def check_mult(c):
  #check result of part a
  endpoint = '{}/{}/{}/{}'.format(API_URL, "mult", my_id, c)
  response = requests.put(endpoint) 	
  print(response.json())

def check_inv(a_inv):
  #check result of part b
  response = requests.put('{}/{}/{}/{}'.format(API_URL, "inv", my_id, a_inv)) 
  print(response.json())

a, b = get_poly()
##SOLUTION  
a_vec  = BitVector(bitstring = a)
b_vec  = BitVector(bitstring = b)
poly = BitVector(bitstring = '100011011')
check_mult(a_vec.gf_multiply_modular(b_vec, poly, 8))
check_inv(a_vec.gf_MI(poly, 8))



