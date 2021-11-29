# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 12:57:41 2021

@author: user
"""

import math
import warnings
import sympy
import random
import requests

#API_URL = 'http://10.36.52.109:6000'
API_URL = 'http://cryptlygos.pythonanywhere.com'

my_id = 25331

def getQ1():
  endpoint = '{}/{}/{}'.format(API_URL, "Q1", my_id )
  response = requests.get(endpoint) 	
  if response.ok:	
    res = response.json()
    print(res)
    n, t = res['n'], res['t']
    return n,t
  else: print(response.json())
  
  
def checkQ1a(order):   #check your answer for Question 1 part a
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1a", my_id, order)
  response = requests.put(endpoint) 	
  print(response.json())
  

def checkQ1b(g):  #check your answer for Question 1 part b
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1b", my_id, g)	#gH is generator of your subgroup
  response = requests.put(endpoint) 	#check result
  #print(response.json()) 
  return response.json()
 
    
def checkQ1c(gH):  #check your answer for Question 1 part c
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1c", my_id, gH )	#gH is generator of your subgroup
  response = requests.put(endpoint) 	#check result
  print(response.json())
  
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
  
# # Question 1 Part A
n, t = getQ1()
print("Returned values n and t: {}, {}".format(n,t))
print("Is my 'n = {}' prime number?: {}".format(n, sympy.isprime(n)))
checkQ1a(418)

# Question 1 Part B
my_group = set(range(1, n))
generators = []
for i in range(1, n):
    my_list = set({})
    for k in range(1, n):
        val = (i ** k) % n
        my_list.add(val)
    if my_list == my_group:
        generators.append(i)
        
print("\nNumber of generators should be {} according to phi function of n-1 = {}".format(phi(n-1), n-1))
print("Number of generators of my group according to my algorithm: {}".format(len(generators)))
print("Smallest 5 generators of my group: {}".format(generators[:5]))
print("Check Question 1b response from server")
print("Given generator is -> {}, corresponding response from server -> {}".format(generators[0], checkQ1b(generators[0])))
print("Given generator is -> {}, corresponding response from server -> {}".format(generators[1], checkQ1b(generators[1])))
print("All of the generators: ", generators)

# Question 1 Part C
for i in range(1,n):
    my_list = set({})
    for k in range(1,n):
        val = (i ** k) % n
        my_list.add(val)
    if len(my_list) == t:
        print("\nThis is the order t = {} subgroup: {}".format(t, my_list))
        break

my_subgroup = my_list
generators = []
for i in my_list:
    temp = set({})
    for k in range(1,n):
        val = (i ** k) % n
        temp.add(val)
    if temp == my_subgroup:
        generators.append(i)
print("Generators of my sub group: {}".format(generators))
checkQ1c(300)

# for k in my_list:
#     temp = []
#     for m in my_list:
#         val = (k * m) % n
#         temp.append(val)
#     print(temp)
















