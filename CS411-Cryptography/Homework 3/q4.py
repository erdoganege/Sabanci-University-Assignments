# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 00:24:06 2021

@author: user
"""

import math
from sympy import *
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
    

n = 237540380304900134239
c = 226131284405640469226
e = pow(2,16) + 1


for i in range(1,n,2):
    if n%i == 0:
        print("Found a factor!", i)
        if isprime(i) == True:
            if isprime(int(n/i)) == True:
                       p = i
                       q = int(n/i)
            break

print("Our p: ", p)
print("Our q: ", q)

phi_n = (p-1) * (q-1)
d = modinv(e, phi_n)

m_ = pow(c, d, n)
print("Corresponding message:", m_.to_bytes((m_.bit_length() + 7) // 8, 'big').decode()[::-1])



