#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#x is used as filler alphabet and needs to be ignored in the output of decrypt function
import numpy as np
def creatematrix(plaintxt,key):
    a=len(plaintxt)//len(key)
    if len(plaintxt)%len(key)!=0:
        for i in range(len(key)*(a+1)-len(plaintxt)):
            plaintxt+='x'
        return np.array(list(plaintxt)).reshape(a+1,len(key))
    return np.array(list(plaintxt)).reshape(a,len(key))

def encrypt(matrix,key):
    ciphertxt=''
    for i in range(len(key)):
        c=key.index(i+1)
        ciphertxt+=''.join(matrix[:,c])
    return ciphertxt

def decrypt(ciphertxt,key):
    cc=''
    c=len(ciphertxt)//len(key)
    for i in key:
        cc+=ciphertxt[(i-1)*c:(i-1)*c+c]
    a=np.array(list(cc)).reshape(len(key),c).T
    return ''.join(a.reshape(1,len(ciphertxt)).tolist()[0])
    
plaintxt=input('Enter your plain text here: ')
key=list(map(int,input().split()))
m=creatematrix(plaintxt,key)
ciphertxt=encrypt(m,key)
print(m)
print('Your ciphered text is: ',ciphertxt)
print('Your deciphered text is:',decrypt(ciphertxt,key))

