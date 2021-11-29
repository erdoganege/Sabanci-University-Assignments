#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:46:33 2021

@author: ozgur
"""
import matplotlib.pyplot as plt
# import numpy as np

cipher_text = "Iur tvlrc ig vnc wof il tvps aoiutpy wu wfiqo ajl aln yrs jrcahld cqihl-rhsye gs cue \
fuahn gngairuhpol tvht kayls y pobpcr hoe cqihl mf o Yoaksmejlsy, tfe gaunir tal tvl \
eouos od ab Lilshlil, abk tfe wnnmrout kab ahc eebaj ot hnw ccslcgs wrcswkelt. Hoar \
ibztgtiaimn, ulnrlstel, ig h cmufa. Ir cou bc tvl Sspflmc Ccbrr ot ahc Ubptcd Saareg vr \
rhs oukbzlsr J.D josrh pn rhs sald, cy tfig oolofhbje qvupt koiah mvu qefce. Muf josrhz \
hyvs ahcif maslhz, aq dcls ynm oukab pnqtwauricu, bst wu tfig josnhyy muf josrhz \
ape hoe ersht jejllcrg, hnb ib vup ccbrrs osl keb hrc cflarer lqsaz. P'm lo wkeylwzt \
ro pllgejl fgrasy gn hoe gnhlgpihf od oiy cmufas ynr pn rhs \
qupy-gfsrea ahyt wz nm irlaj tc te, gt wz a jijpne, wcykgnu yeylway. Eebalcmsu, a \
aoiyt gs bv bcthlr rhou eycv tal ot fos swatgnu iedofl mc ob ahgs xbrw. A qvupt wz \
ollm hs qoiud ys was huff, ald o qupy wz ollm hs qoiud ys hoe keb dhm more gt iw. I \
ym qvndirlnr tvht woi neltzlmcn kplj rscicw kptfoia pysgpol tvl etirlnae mvu fajl hcafk, \
cmms ao y dsjiqicu, ald flsrofl tfig kedebkalt hv hgs thmglm. Pn rhs uake cm Gmd, rv \
ymuf kury."

uppercase ={'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8,
         'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16,
         'R':17, 'S':18,  'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24,
         'Z':25}
inv_uppercase = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
                 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P',
                 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X',
                 24:'Y', 25:'Z'}

letter_count = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0,
              'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0,
              'R':0, 'S':0,  'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

uppercase_keys = list(uppercase.keys())    
max_key_length = 11



#Modify cipher_text to get rid of non-alphabetic characters
modified_cipher = ""
for i in range(len(cipher_text)):
    if cipher_text[i].upper() in uppercase_keys:
        modified_cipher += cipher_text[i].upper()


coincidence_counts = []
coincidence_letters = []
for i in range(max_key_length):
    count = 0
    temp = ''
    # temp2 = np.zeros(26)
    for m in range(i):
        temp += 'x'
    temp += modified_cipher
    for j in range(i, len(modified_cipher)):
        if temp[j] == modified_cipher[j]:
            # temp2[uppercase[temp[j]]] += 1 
            count += 1
    coincidence_counts.append(count)
    # coincidence_letters.append(temp2)
    
    
plt.bar(range(1,11), coincidence_counts[1:])
plt.title("Number of coincidences for different shift amounts")
plt.ylabel("Number of Coincidences")
plt.xlabel("Shift Amount")

#Obtain sub-cipher texts
sub_ciphers = []
for i in range(5):
    text = ""
    for k in range(i, len(modified_cipher), 5):
        text += modified_cipher[k]
    sub_ciphers.append(text)

#frequency analysis of each sub-cipher texts
sub_cipher_counts = []
for k in sub_ciphers:
    letter_count = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0,
              'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0,
              'R':0, 'S':0,  'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    for i in k:
        letter_count[i] += 1
    sub_cipher_counts.append(letter_count)
    letter_count = {}

index = 1
sub_ciphers_possible_keys = []
for i in sub_cipher_counts:
    possible_keys = []
    sorted_temp = {k: v for k, v in sorted(i.items(), key=lambda item: item[1])}   #taken from StackOverflow     
    sorted_keys = list(sorted_temp.keys())
    sorted_values = list(sorted_temp.values())
    print("\n{}. sub cipher text analysis:".format(index))
    
    print("Most 5 frequent letters {}, and their counts {} \nLeast 5 frequent letters {}, and their counts {}".format(\
        sorted_keys[-5:], sorted_values[-5:], sorted_keys[:5], sorted_values[:5]))
    
    for k in ['E', 'T', 'A', 'O']:
        print("Mapping most frequent letter {} into {}:".format(sorted_keys[-1],k))
        possible_key = (uppercase[sorted_keys[-1]] - uppercase[k]) % 26
        print("Key value = {}".format(possible_key))
        possible_keys.append(possible_key)
    print("Possible keys for k{}: {}".format(index, possible_keys))
    index += 1
    sub_ciphers_possible_keys.append(possible_keys)
    
    for m in possible_keys:
        most_letters = []
        least_letters = []
        for j in range(5,0,-1):
            letter = sorted_keys[-j]
            new_letter = inv_uppercase[(uppercase[letter] - m) % 26]
            most_letters.append(new_letter)
        for j2 in range(5):
            letter = sorted_keys[j2]
            new_letter = inv_uppercase[(uppercase[letter] - m) % 26]
            least_letters.append(new_letter)            
        print("\nIf we choose key length as {}:".format(m))
        print("Most frequent letters  {} are mapped to ==> {}".format(sorted_keys[-5:], most_letters))
        print("Least frequent letters {} are mapped to => {}".format(sorted_keys[:5], least_letters))
        
    
    
key = [7, 0, 24, 0, 14]
plain_text = ''
k = 0
for i in range(len(cipher_text)):
    if cipher_text[i].upper() in uppercase.keys():
        index = k % 5    
        k += 1
        new_letter = (uppercase[cipher_text[i].upper()] - key[index]) % 26
        plain_text += inv_uppercase[new_letter]
    else:
        plain_text += cipher_text[i]    
        
print("\nPlain text:", plain_text)
    
    
    

   
    
# #Obtain 7 sub-cipher texts
# sub_ciphers = []
# for i in range(7):
#     text = ""
#     for k in range(i, len(modified_cipher), 7):
#         text += modified_cipher[k]
#     sub_ciphers.append(text)

# #frequency analysis of each sub-cipher texts
# sub_cipher_counts = []
# for k in sub_ciphers:
#     letter_count = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0,
#               'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0,
#               'R':0, 'S':0,  'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
#     for i in k:
#         letter_count[i] += 1
#     sub_cipher_counts.append(letter_count)
#     letter_count = {}

# index = 1
# sub_ciphers_possible_keys = []
# for i in sub_cipher_counts:
#     possible_keys = []
#     sorted_temp = {k: v for k, v in sorted(i.items(), key=lambda item: item[1])}   #taken from StackOverflow     
#     sorted_keys = list(sorted_temp.keys())
#     sorted_values = list(sorted_temp.values())
#     print("\n{}. sub cipher text analysis:".format(index))
    
#     print("Most 5 frequent letters {}, and their counts {} \nLeast 5 frequent letters {}, and their counts {}".format(\
#         sorted_keys[-5:], sorted_values[-5:], sorted_keys[:5], sorted_values[:5]))
    
#     for k in ['E', 'T', 'A', 'O']:
#         print("Mapping most frequent letter {} into {}:".format(sorted_keys[-1],k))
#         possible_key = (uppercase[sorted_keys[-1]] - uppercase[k]) % 26
#         print("Key value = {}".format(possible_key))
#         possible_keys.append(possible_key)
#     print("Possible keys for k{}: {}".format(index, possible_keys))
#     index += 1
#     sub_ciphers_possible_keys.append(possible_keys)
    
#     for m in possible_keys:
#         most_letters = []
#         least_letters = []
#         for j in range(5,0,-1):
#             letter = sorted_keys[-j]
#             new_letter = inv_uppercase[(uppercase[letter] - m) % 26]
#             most_letters.append(new_letter)
#         for j2 in range(5):
#             letter = sorted_keys[j2]
#             new_letter = inv_uppercase[(uppercase[letter] - m) % 26]
#             least_letters.append(new_letter)            
#         print("\nIf we choose key length as {}:".format(m))
#         print("Most frequent letters  {} are mapped to ==> {}".format(sorted_keys[-5:], most_letters))
#         print("Least frequent letters {} are mapped to => {}".format(sorted_keys[:5], least_letters))
        
    
    
# key = [4, 0, 0, 4, 6, 11, 20]
# plain_text = ''
# k = 0
# for i in range(len(cipher_text)):
#     if cipher_text[i].upper() in uppercase.keys():
#         index = k % 7
#         k += 1
#         new_letter = (uppercase[cipher_text[i].upper()] - key[index]) % 26
#         plain_text += inv_uppercase[new_letter]
#     else:
#         plain_text += cipher_text[i]    
        
# print("\nPlain text:", plain_text)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        











    



































        
        
