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

def encrypt(creatematrix,matrix,key):
    ciphertxt1=''
    for i in range(len(key)):
        c=key.index(i+1)
        ciphertxt1+=''.join(matrix[:,c])
    print('Your single encrypted text is: ',ciphertxt1)
    a=creatematrix(ciphertxt1,key)
    ciphertxt2=''
    for i in range(len(key)):
        k=key.index(i+1)
        ciphertxt2+=''.join(a[:,k])
    return ciphertxt2

def decrypt(ciphertxt,key):
    cc=''
    cc1=''
    cc2=''
    c=len(ciphertxt)//len(key)
    for i in key:
        cc+=ciphertxt[(i-1)*c:(i-1)*c+c]
    a=np.array(list(cc)).reshape(len(key),c).T
    cc1=''.join(a.reshape(1,len(ciphertxt)).tolist()[0])
    print('Your single decrypted text is:',cc1)
    for i in key:
        cc2+=cc1[(i-1)*c:(i-1)*c+c]
    aa=np.array(list(cc2)).reshape(len(key),c).T
    return ''.join(aa.reshape(1,len(ciphertxt)).tolist()[0])
    
plaintxt=input('Enter your plain text here: ')
key=list(map(int,input().split()))
m=creatematrix(plaintxt,key)
print(m)
ciphertxt=encrypt(creatematrix,m,key)
print('Your double encrypted text is:',ciphertxt)
print('Your double decrypted text is:',decrypt(ciphertxt,key))

