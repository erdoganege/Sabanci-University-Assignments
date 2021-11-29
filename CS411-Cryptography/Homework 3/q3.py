# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 20:03:13 2021

@author: user
"""
import copy 
import itertools

def LFSR(C, S):
    L = len(S)
    fb = 0
    out = S[L-1]
    for i in range(0,L):
        fb = fb^(S[i]&C[i+1])
    for i in range(L-1,0,-1):
        S[i] = S[i-1]

    S[0] = fb
    return out

def find_all_states(n, i):
    all_states = list(map(list, itertools.product([0, 1], repeat=n-1)))
    return all_states

def coincidence_count(n, temp,C,z):
    count_list = []   
    all_states = find_all_states(n,temp)
    for k in all_states:
        key = []
        count = 0
        # print("State:", k)
        # print("Polynom:", C)
        for i in range(len(z)):
            key.append(LFSR(C,k))
            # print("State: ", k)
            # print("Key:", key)
        for m in range(len(z)):
            if key[m] == z[m]:
                count += 1
        
        count_list.append(count)
    return count_list
    
def geffe(s1, s2, s3):
    z_test = (s1 and s2) ^ (s2 and s3) ^ s3
    return z_test

z = [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0]

C1 = [0] * 8
for i in [0,5,7]:
    C1[i] = 1

C2 = [0] * 14
for i in [0,3,7, 13]:
    C2[i] = 1
    
C3 = [0] * 12
for i in [0,2,11]:
    C3[i] = 1
    
    
print("Length of z: ",len(z))    
state_list1 = find_all_states(8,1)
print("Number of possible states for LFSR{} = {}".format(1,len(state_list1)))
count_list1 = coincidence_count(8, 1,C1,z)

print("Maximum coincidences for LFSR1: ", max(count_list1))
print("Corresponding state: ", state_list1[count_list1.index(max(count_list1))])

state_list3 = find_all_states(12,3)
print("Number of possible states for LFSR{} = {}".format(3,len(state_list3)))
count_list3 = coincidence_count(12, 3,C3,z)

print("Maximum coincidences for LFSR3: ", max(count_list3))
print("Corresponding state: ", state_list3[count_list3.index(max(count_list3))])

state_list2 = find_all_states(14,2)
print("Number of possible states for LFSR{} = {}".format(2,len(state_list2)))
count_list2 = coincidence_count(14, 2,C2,z)

S1 = [0, 1, 1, 1, 1, 1, 0]
key1 = []
for i in range(len(z)):
    key1.append(LFSR(C1,S1))
    
S3 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
key3 = []
for i in range(len(z)):
    key3.append(LFSR(C3,S3))



for k in state_list2:
    final = k.copy()
    key2 = []
    for i in range(len(z)):
        key2.append(LFSR(C2,k))
    z2 = []
    for m in range(len(z)):
        z2.append(geffe(key1[m], key2[m], key3[m]))
    if z2 == z:
        print("WOW", final)
        
S2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
key2 = []
for i in range(len(z)):
    key2.append(LFSR(C2,S2))
result = []
for i in range(len(z)):
    result.append(geffe(key1[i], key2[i], key3[i]))
    if result == z:
        print("Proved!")
print("LFSR1 initial state: ", S1)
print("LFSR2 initial state: ", S2)
print("LFSR3 initial state: ", S3)





