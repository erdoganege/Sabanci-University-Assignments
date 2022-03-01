# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 23:23:16 2021

@author: user
"""

from DSA import *

q = 1274928665248456750459255476142268320222010991943
p = 94399082877738640356344835093633851742226810946548058167594106609599304101483376198601628644645578978665867743371516213549559017509270013785262825124888169738692088560919995075509146379802866347021353299579995280712578946802331952341703103059527013530389111994085951544456654086033481582042901134498773988127
g = 74757613048887093209741634228228425902948572222965683892966782829654298800791789084861356704346371244921201938818880899647348974925451953450279300514594642896343751389085838466583384452902564477981127117505259585303938871436241327714244689153971542398500058515599232922200606171788427214873986464441516423273
beta = 9391078822012222264248483853957955450074521847096866533459681369546944886235023857738438187102424298184377435789154539420500484576343932422250732759800837979336463896251863203597988162906413924736488554239908614170057127399588501615428907239954984946982024571938034476806841633488050802767414373595444261997

m1 = b'Erkay hoca wish that you did learn a lot in the Cryptography course'
r1 = 780456265196245442017019073827244628033034896446
s1 = 214154189471546244965139202160125045302874348377

m2 = b'Who will win the 2021 F1 championship, Max or Lewis?'
r2 = 927294142715241205623350780659879368622965215767
s2 = 151110642214296558517943730901561426792280910589


if (r1 == r2):
    print("Same k is used for encryption which is a fatal!")  
shake = SHAKE128.new(m1)
h1 = int.from_bytes(shake.read(q.bit_length()//8), byteorder='big')
shake = SHAKE128.new(m2)
h2 = int.from_bytes(shake.read(q.bit_length()//8), byteorder='big')
x = 1
while True:
    temp = modinv(abs(s2*r1*x - s1*r2), q)
    a = ((s1*h2 - s2*h1*x)*temp)%q
    if pow(g,a,p) == beta:
        print("We have found the x:",x)
        print("Corresponding secret key a:", a)
        break
    else:
        x += 1

print("Lets verify this is a true secret alpha key value!")
s2_inv = modinv(s2, q)
k = (s2_inv*(h2+ a*r1))%q
print("My k value: ", k)
r, s = Sig_Gen(m1, a, k, q, p, g)
if Sig_Ver(m1, r, s, beta, q, p, g):
    print("signature verifies:) ")
else:
    print("invalid signature:( ")  
    
    