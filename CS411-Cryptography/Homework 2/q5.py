# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:52:12 2021

@author: user
"""



def shift(pol, new_bit):
    temp = []
    temp.append(new_bit)
    for i in range(len(pol)-1):
        temp.append(pol[i])
    return temp

# Polynom 1 -> x^5 + x^2 + 1

S1 = [0,0,0,0,1] 
initial = S1.copy()
print("Initial state: {}".format(initial))
for i in range(2**len(S1)-1):
    S1 = shift(S1, S1[1]^S1[4])
    print("{}. state: {}".format(i+1, S1))    
    if S1 == initial:
        print("We completed our cycle in {} states".format(i+1))
        break
if i+1 == 2**len(S1)-1:
    print("Connection polynomial for LFSR produces maximum period sequence!")
else:
    print("It does not produce maximum period sequence!")
    
    
# Polynom 2 -> x^5 + x^3 +x^2 + 1

S1 = [0,0,0,0,1] 
initial = S1.copy()

print("\nInitial state: {}".format(initial))
for i in range(2**len(S1)-1):
    S1 = shift(S1, S1[1]^S1[4]^S1[2])
    print("{}. state: {}".format(i+1, S1))    
    if S1 == initial:
        print("We completed our cycle in {} states".format(i+1))
        break
if i+1 == 2**len(S1)-1:
    print("Connection polynomial for LFSR produces maximum period sequence!")
else:
    print("It does not produce maximum period sequence!")