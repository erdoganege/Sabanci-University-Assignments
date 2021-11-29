# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 18:56:52 2021

@author: user
"""


# Do not forget to install pycryptodome if not already installed
# pip install pycryptodome

import random
from Crypto.Hash import SHA3_256
from Crypto import Random
import json

def Reduction(x, Alphabet, length, i):
  pwd = ""
  t = x+i
  size = len(Alphabet)
  for j in range(0,length):
    pwd += Alphabet[t%size]
    t = t >> 5
  return pwd

Alphabet = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}
alpha_len = len(Alphabet)
pwd_len = 6
pwd_space = alpha_len**pwd_len 
t = 2**16+1
m = 2*(pwd_space//t)


# # Example for computing one link in the chain; i.e., pwd(i+1) = R(H(pwd(i)))
# print("This is how you compute one link in the hash chain")
# i=0 #ith password
# pwd_i = "ERKAYS"
# hash = SHA3_256.new(pwd_i.encode('utf-8')) # hash it
# digest = int.from_bytes(hash.digest(), byteorder='big') # convert the hash into an integer
# pwd_i1 = Reduction(digest%pwd_space, Alphabet, pwd_len, i) # Reduce it

# # Read the rainbow table
with open("C:/Users/user/Desktop/cs411_507_hw03_erdoganege/rainbowtable.txt","r") as f: #Change PATH While TESTING
    Rainbow_Table = [i.strip("\n").split(" ") for i in f]


# # Digests
digestt = [0]*10
digestt[0] = 22124189486495673593367569540475592102282157979290438299810565423533928140608
digestt[1] = 113038931731002281515368045561041771452890345577521779347806994396802366165143
digestt[2] = 16490946906972051103239208910401321977744447164149216527605537227006563531014
digestt[3] = 105353391397460238951220522764807459073515234831240339048337973998116727230996
digestt[4] = 26563289533287154151815787500875213883490536719930521098682624545687449677034
digestt[5] = 9069125006391660627263185490215282859879233050573029398056289720760246452345
digestt[6] = 85142502917963023098581159157468363727708090026370245682837279337011466335140
digestt[7] = 38334754424989293872789263165471906081000373205278872976990878833048663314631
digestt[8] = 74006848995374687719545698110937576674231736916380406212520942778884501038555
digestt[9] = 61355375510981975738745517654773760277485454500890040709780777001440346981129


###
for org_digest in digestt:
    seq = 0
    temp = Reduction(org_digest%pwd_space, Alphabet, pwd_len, seq)
    for i in range(len(Rainbow_Table)):
        if temp == Rainbow_Table[i][1]:
            print("YES CASE 1 APPLY")
            initial_pwd = Rainbow_Table[i][0]
            seq2 = 0
            print("Corresponding Initial Block: ", initial_pwd)
            for k in range(t-1):
                hash = SHA3_256.new(initial_pwd.encode('utf-8')) # hash it
                temp_digest = int.from_bytes(hash.digest(), byteorder='big') # convert the hash into an integer
                initial_pwd = Reduction(temp_digest%pwd_space, Alphabet, pwd_len, seq2) 
                seq2 += 1
            hash = SHA3_256.new(initial_pwd.encode('utf-8')) # hash it
            temp_digest = int.from_bytes(hash.digest(), byteorder='big') # convert the hash into an integer    
            print("PROVING!")
            if org_digest == temp_digest:
                print("Corresponding Password: ", initial_pwd)    
       
    seq = 0    
    pwd = Reduction(org_digest%pwd_space, Alphabet, pwd_len, seq)   
    myflag = True
    while myflag:
        myflag2 = True
        hash = SHA3_256.new(pwd.encode('utf-8'))
        digest = int.from_bytes(hash.digest(), byteorder='big')
        seq += 1
        pwd = Reduction(digest%pwd_space, Alphabet, pwd_len, seq) 
        for i in range(len(Rainbow_Table)):
            if pwd == Rainbow_Table[i][1]:
                initial_pwd = Rainbow_Table[i][0]
                print("YES CASE 2 APPLY")
                print("Corresponsing Initial block: ",initial_pwd)     
                myflag = False
                for seq in range(pwd_space):
                    hash = SHA3_256.new(initial_pwd.encode('utf-8'))
                    digest = int.from_bytes(hash.digest(), byteorder='big')  
                    if digest == org_digest:
                        print("Corresponding Password: ", initial_pwd)
                        break
                    initial_pwd = Reduction(digest%pwd_space, Alphabet, pwd_len, seq)
                break
       
        

