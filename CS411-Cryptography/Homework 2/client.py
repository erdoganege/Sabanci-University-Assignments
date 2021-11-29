import random
import requests

#API_URL = 'http://10.36.52.109:6000'
API_URL = 'http://cryptlygos.pythonanywhere.com'

my_id = 11111   

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
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1b", my_id, g )	#gH is generator of your subgroup
  response = requests.put(endpoint) 	#check result
  print(response.json())

def checkQ1c(gH):  #check your answer for Question 1 part c
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1c", my_id, gH )	#gH is generator of your subgroup
  response = requests.put(endpoint) 	#check result
  print(response.json())


def getQ2():
  endpoint = '{}/{}/{}'.format(API_URL, "Q2", my_id )
  response = requests.get(endpoint) 	
  if response.ok:	
    res = response.json()
    e, cipher = res['e'], res['cipher']
    return e, cipher
  else:  print(response.json())

def checkQ2(ptext):  #check your answer for Question 1 part c
  response = requests.put('{}/{}'.format(API_URL, "checkQ2"), json = {"ID": my_id, "msg":ptext})
  print(response.json())