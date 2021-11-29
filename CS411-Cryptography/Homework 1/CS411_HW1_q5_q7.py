#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:17:02 2021

@author: ozgur
"""
import math
import random
import fractions
import nltk
nltk.download('words')
from nltk.corpus import words
# This is method to compute Euler's function
# The method here is based on "counting", which is not good for large numbers in cryptography
def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            alpha_values.append(k)
            amount += 1
    return amount

# The extended Euclidean algorithm (EEA)
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# Modular inverse algorithm that uses EEA
def modinv(a, m):
    if a < 0:
        a = m+a
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

# You can use the the following variables for encoding an decoding of English letters    

uppercase ={'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8,
         'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16,
         'R':17, 'S':18,  'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24,
         'Z':25, '.':26, ' ':27}



inv_uppercase = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
                 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P',
                 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X',
                 24:'Y', 25:'Z', 26:'.', 27:' '}

def encryptcode(text):
    code = uppercase[text[0]] * 28 + uppercase[text[1]] 
    return code

def decryptcode(code):
    second_char_code = code % 28
    first_char_code = (code - second_char_code) // 28
    
    text = ''
    second_char = inv_uppercase[second_char_code]
    first_char = inv_uppercase[first_char_code]
    text = first_char + second_char
    return text

def Affine_Dec(ctext, key):
    y = encryptcode(ctext)
    x = (key.gamma*y + key.theta) % 784
    ptext = decryptcode(x)
    return ptext
    
    

# key object for Affine cipher
# (alpha, beta) is the encryption key
# (gamma, theta) is the decryption key
class key(object):
    alpha=0
    beta=0
    gamma=0
    theta=0

biagrams = 28*28
modulus = biagrams
print("Number of possible biagrams, and modulus:", 28*28)

print("Alpha should be invertible")
alpha_values = []

amount = phi(modulus)
print("Possible alpha values:", amount)
print("Possible beta values:", biagrams)

print("Size of the key space is:", biagrams * amount)



cipher_text = "RYHUHBCMNHLMHHUYWMNXDIXMR.HUGB RCMD.HMZHOTJYUYWMZJOBBE"


known_plaintext = ".X"
known_ciphertext = "BE"

known_encryptcode = uppercase[known_plaintext[0]] * 28 + uppercase[known_plaintext[1]] 
known_decryptcode = uppercase[known_ciphertext[0]] * 28 + uppercase[known_ciphertext[1]] 

print("Last two characters of plaintext {} and corresponding code {}".format(known_plaintext, known_encryptcode))
print("Last two characters of ciphertext {} and corresponding code {}".format(known_ciphertext, known_decryptcode))


possible_alphabetapairs = []

for i in alpha_values:
    for k in range(biagrams+1):
        result = (known_encryptcode*i + k) % modulus 
        if result == known_decryptcode:
            possible_alphabetapairs.append([i,k])
            
            
            
ciphertext_biagrams = []
for i in range(0,len(cipher_text),2):
    temp = cipher_text[i:i+2]
    ciphertext_biagrams.append(temp)



for i in possible_alphabetapairs:
    key.alpha = i[0]
    key.beta = i[1]
    key.gamma = modinv(key.alpha, 784)
    key.theta = 784-(key.gamma*key.beta)%784
    count = 0
    result = ""
    for k in ciphertext_biagrams:
        ptext = Affine_Dec(k, key)
        result += ptext
        
    sentence = result.split() 
    if sentence[0].lower() in words.words():
            count += 1
    if count >= 1:
        print("alpha {}, beta {}, gamma {}, theta {}, decrypted text {}: ".format(key.alpha, key.beta, key.gamma, key.theta, result))




















