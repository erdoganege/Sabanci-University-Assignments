# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 15:57:43 2021

@author: user
"""
import math
def gcd(a, b):
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
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
def solve(n, a, b):
  my_gcd = gcd(a, n)
  print("Gcd of a and n is: ", my_gcd)
  if (my_gcd == 1):
      print("There is exactly one solution!")
      x = (modinv(a, n) * b) % n
      return x
  else:
      if (b % my_gcd) == 0:
          print("There are {} solutions!".format(my_gcd))
          results = []
          new_a = a // my_gcd
          new_b = b // my_gcd
          new_n = n // my_gcd
          x = (modinv(new_a, new_n) * new_b) % new_n
          for i in range(my_gcd):
              x_ = x + (i * new_n) 
              results.append(x_)
          return results
      else:
          print("{} does not divide {}".format(my_gcd, b))
          return "SOLUTION DOES NOT EXIST"
#Part A
n = 100433627766186892221372630785266819260148210527888287465731
a = 336819975970284283819362806770432444188296307667557062083973
b = 25245096981323746816663608120290190011570612722965465081317
result = solve(n,a,b)
print("Result: {}\n".format(result))
#Part B
n = 301300883298560676664117892355800457780444631583664862397193
a = 1070400563622371146605725585064882995936005838597136294785034
b = 1267565499436628521023818343520287296453722217373643204657115
result = solve(n,a,b)
print("Result: {}\n".format(result))
#Part C
n = 301300883298560676664117892355800457780444631583664862397193
a = 608240182465796871639779713869214713721438443863110678327134
b = 721959177061605729962797351110052890685661147676448969745292
result = solve(n,a,b)
print("Result: {}\n".format(result))










