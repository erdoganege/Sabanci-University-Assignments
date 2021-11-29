import requests # if this lib isn't installed yet --> pip install requests or pip3 intall requests

import math
import random
import fractions

# This is method to compute Euler's function
# The method here is based on "counting", which is not good for large numbers in cryptography
def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
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
    
# You can use the Turkish alphabet for Question 3
# Note that encyrption and decryption algorithms are slightly different for
# Turkish texts
turkish_alphabet ={'A':0, 'B':1, 'C':2, 'Ç':3, 'D':4, 'E':5, 'F':6, 'G':7, 'Ğ':8, 'H':9, 'I':10,
         'İ': 11, 'J':12, 'K':13, 'L':14, 'M':15, 'N':16, 'O':17, 'Ö':18, 'P':19, 
         'R':20, 'S':21,  'Ş':22, 'T':23, 'U':24, 'Ü':25, 'V':26, 'Y':27,
         'Z':28, '.':29, ',':30}

inv_turkish_alphabet = {0:'A', 1:'B', 2:'C', 3:'Ç', 4:'D', 5:'E', 6:'F', 7:'G', 8:'Ğ', 9:'H',
              10:'I', 11:'İ', 12:'J', 13:'K', 14:'L', 15:'M', 16:'N', 17:'O', 18:'Ö',
              19:'P', 20:'R', 21:'S',  22:'Ş', 23:'T', 24:'U', 25:'Ü', 26:'V',
              27:'Y', 28:'Z', 29:'.', 30:','}

letter_count = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0,
         'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0,
         'R':0, 'S':0,  'T':0, 'U':0, 'V':0, 'Y':0, 'Z':0, 'Ç':0, 'Ğ':0, 'İ':0, 'Ö':0, 'Ş':0, 'Ü':0, '.':9, ',':0}


def Affine_Dec(ptext, key):
    plen = len(ptext)
    ctext = ''
    for i in range (0,plen):
        letter = ptext[i]
        if letter in turkish_alphabet:
            poz = turkish_alphabet[letter]
            poz = (key.gamma*poz+key.theta)%31
            ctext += inv_turkish_alphabet[poz]
        else:
            ctext += ptext[i]
    return ctext

# key object for Affine cipher
# (alpha, beta) is the encryption key
# (gamma, theta) is the decryption key
class key(object):
    alpha=0
    beta=0
    gamma=0
    theta=0


### DO NOT CHANGE HERE ######

API_URL = 'http://cryptlygos.pythonanywhere.com' # DO NOT change url 

def getCipher(my_id):
    endpoint = '{}/{}/{}'.format(API_URL, "affine_game", my_id )
    response = requests.get(endpoint) 	#get your ciphertext and most freq. letter
    ctext, letter = "", ""
    if response.ok:	#if you get your ciphertext succesfully
        c = response.json()
        ctext = c[0]    #this is your ciphertext
        letter = c[1] 	#the most frequent letter in your plaintext
    elif(response.status_code == 404):
        print("We dont have a student with this ID. Check your id num")
    else:
        print("It was supposed to work:( Contact your TA")
    
    return ctext, letter
    
    
def sendMessage(my_id, plaintext):    
    endpoint = '{}/{}/{}/{}'.format(API_URL, "affine_game", my_id, plaintext)
    response = requests.put(endpoint)
    if response.ok:
        c = response.json()
        print(c)
    elif(response.status_code == 404):
        print("Nope, Try again")
    elif(response.status_code == 401):
        print("Check your ID number")
    else:
        print("How did you get in here? Contact your TA")
        
###### MOdify below     
    7
if __name__ == '__main__':
    my_id = 25331	# change this to your id number. it should be 5 digit number
    
    cipher_text, most_frequent_letter = getCipher(my_id)
    
    """
    Use the ciphertext and the most frequent letter of the ciphertext
    Find the plaintext.
    And assing it to below variable named plainText 
    If your answer is correct it prints out "Congrats"
    
    """
    for i in range(len(cipher_text)):
        if cipher_text[i] in letter_count.keys():
            letter_count[cipher_text[i]] += 1

    letter_count_keys = list(letter_count.keys())    
    letter_count_values = list(letter_count.values())
    pos = letter_count_values.index(max(letter_count_values)) 
    
    most_frequenct_cipher_letter = letter_count_keys[pos]
    print("Most Frequent letter in cipher text:", most_frequenct_cipher_letter)
    
    possible_alpha_values = []
    for alpha in range(31):
        d, x, y = egcd(alpha, 31)
        if d == 1:
            possible_alpha_values.append(alpha)

    possible_pairs = []
    for i in possible_alpha_values:
        for k in range(31):
            if turkish_alphabet[most_frequenct_cipher_letter] == (i*turkish_alphabet[most_frequent_letter] + k) % 31:
                possible_pairs.append([i,k])
    
    for i in possible_pairs:
        key.alpha = i[0]
        key.beta =  i[1]
        key.gamma = modinv(key.alpha, 31)
        key.theta = 31-(key.gamma*key.beta)%31
        ptext = Affine_Dec(cipher_text, key)    
        print("alpha, beta, gamma, theta, decrypted text: ", key.alpha, key.beta, key.gamma, key.theta, ptext)
    

    plainText = "KESİNLİKLE SON GÜNLERİNİ YAŞIYORDUR, YOKSA ONA AİT OLAN HER ŞEYİ TOPARLAMAK, BANA NE SÖYLEMİŞ VE NE YAPMIŞSA HATIRLAMAK VE KAÇMASINLAR DİYE HEPSİNİ KAĞIDA YANSITMAK KONUSUNDA BANA EGEMEN OLAN ÖNÜ ALINMAZ İSTEĞİ BAŞKA TÜRLÜ AÇIKLAYAMAZDIM SANKİ ÖLÜMÜ, ONUN ÖLÜMÜNÜ KAÇIRMAK İSTİYOR GİBİYİM KORKARIM BU YAZDIĞIM, BİR KİTAP DEĞİL, BİR 'GÜZELLEME' OLACAK VE ŞIMDİ GÖRÜYORUM Kİ BU KİTAP, BİR GÜZELLEMENİN BÜTÜN BELİRTİLERİNİ TAŞIMAKTADIR TEPSİ, KOLİVA VE KALIN BİR ŞEKER TABAKASIYLA SÜSLENMİŞ, ONUN ÜZERİNE DE, TARÇINI VE BADEMLE ALEKSİ ZORBA ADI YAZILMIŞ ADINA BAKIYORUM, BİRDEN SANKİ GİRİT'İN ÇİVİT MAVİSİ DENİZİ ÇALKALANIYOR VE BEYNİM TOPARLANIYOR SÖZLER, GÜLÜŞLER, RAKSLAR, SARHOŞLUKLAR, İKİNDİ ÜSTLERİ ALÇAK SESLE KONUŞMALAR, HER AN BENİ KARŞILIYORMUŞ GİBİ, HER AN BANA VEDA EDİYORMUŞ GİBİ DİKİLEN YUSYUVARLAK, CANLI, ÇEKİNGEN GÖZLER BAŞTAN AŞAĞI SÜSLÜ ÖLÜ TEPSİSİNE BAKTIĞIMIZ ZAMAN, KALBİMIZİN MAĞARASINDA NASIL ANILARIMIZ YARASALAR GİBİ SALKIM SALKIM SARKARSA, ZORBA'NIN GÖLGESI ARKASİNDA, BEN İSTEMEDEN, DÜŞKÜN, ÇOK BOYANMIŞ, ÇOK ÖPÜLMÜŞ, GİRİT'İN LİBYA AÇIĞINDAKİ BİR KUMSALDA ZORBA İLE BİRLİKTE KARŞILAŞTIĞIMIZ BİR KADIN DA, İLK ANDAN BERİ, BEKLENMEDİĞİ HALDE BELİRİVERMİŞTİ"
 
    #Check your answer with this function. 
    sendMessage(my_id, plainText)
    
