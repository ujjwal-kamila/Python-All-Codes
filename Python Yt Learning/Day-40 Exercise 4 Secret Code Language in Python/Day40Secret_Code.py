# Day-40 Exercise 4 Secret Code Language in Python
#This is a code to Create a Secret Language
# '''
# What do i Want with this code?
# To Encrypt the Secret Language like:
#   hello i am Ujjwal kamila ----> hieglplooi lid faamp qubjejtwqaalq lkjaxmiinlsad    #generate a random letter b/w sentance
# To Unencrypt the Secret Language like:
#   hieglplooi lid faamp qubjejtwqaalq lkjaxmiinlsad ----> hello i am ujjwal kamila     # You have to remove every second letter
# '''

import random

def Coding(letter, Made_by_Ujjwal):
  x = 0
  Encrypt = ''
  CodeS = input('Enter Your Sentence: ')
  CodeS = CodeS.lower()
  for i in CodeS:
    Encrypt = Encrypt + CodeS[x]
    x += 1
    for j in range(1):
      Encrypt = Encrypt + random.choice(letter)  
  print(f'\n\n{Made_By_Ujjwal.center(70,".")}')
  print(f'Here is your Encrypted Massage: {Encrypt}')
  input()
  print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

#Decoding 
def Decoding(Made_by_Ujjwal):    #
  x = -2
  Unencrypt = ''
  CodeS = input('Enter Your Sentence: ')
  Codes = CodeS.lower()
  for i in CodeS:
    x += 2
    try:
      Unencrypt = Unencrypt + CodeS[x]
    except:
      print(f'\n\n{Made_By_Ujjwal.center(70,".")}')
      print(f'Here is your Unencrypted Massage: {Unencrypt}')
      input()
      print('\n\n\n\nn\n\n\n\n\n\n')
      break
      

#Asking User about what he wants to do (Coding/Decoding) 
letter_num = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
End_Greetings = 'Thank You for using this Program'
Made_By_Ujjwal = 'Made by Ujjwal kamila '
for i in range(100):
  Choose = input("Do you want convert massage into 'Code' or 'Decode' / Do you to 'Exit'?\n")
  Choose = Choose.lower()
  if Choose == "code":
    Coding(letter_num, Made_By_Ujjwal)
  elif Choose == "decode":
    Decoding(Made_By_Ujjwal)
  elif Choose == "exit":
    print(f'\n\n{End_Greetings.center(70,".")}')
    print(f'{Made_By_Ujjwal.center(70,".")}')
    input()
    exit()
  else:
    print("Please!!!, Enter your choose with Proper Spelling")
    
#Coding:     'hi sir' --> 'hgid assibrh'
#Decoding:   'hgid assibrh' --> 'hi sir''