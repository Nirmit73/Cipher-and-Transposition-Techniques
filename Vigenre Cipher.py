#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def encrypt(plaintxt,key):
    l=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ciphertxt=''    
    for i in range(len(key)):
        ciphertxt+=l[(ord(plaintxt[i])+ord(key[i]))%26]
    return ciphertxt    
def decrypt(ciphertxt,key):
    l=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    plaintxt=''
    for i in range(len(key)):
            plaintxt+=l[(ord(ciphertxt[i])-ord(key[i]))%26]
    return plaintxt

plaintxt=''.join(input('Enter plain text here: ').upper().split())
key=input('Enter the keyword: ').upper()

if len(plaintxt)!=len(key):
    count=0
    
    while len(plaintxt)!=len(key):
        if count>=len(key):
            count=0
        key+=key[count]
        count+=1    
        
ciphertxt=encrypt(plaintxt,key)
plaintxt=decrypt(ciphertxt,key)
print('Your Ciphered text is: ',ciphertxt)
print('Your plain text is: ',plaintxt)

