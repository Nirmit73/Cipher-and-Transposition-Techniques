#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Works for numerical message only
#Your product of p and q must be greater than the message
from math import gcd
import random
def RSA_Encrypt(M,p,q):
    n=p*q
    phin=(p-1)*(q-1)
    l=[]
    for i in range(2,phin):
        if gcd(phin,i)==1:
            l.append(i)
    e=random.sample(l,1)[0]
    d=1
    while (e*d)%phin!=1:
        d=d+1    
    C=1
    for i in range(e):
        C=((C*M)%n)%n 
    return C,n,e,d

def RSA_Decrypt(C,n,e,d):
    m=1
    for i in range(d):
        m=((m*C)%n)%n
    return m


M=int(input('Enter a message: '))
p=int(input('Enter a prime number: '))
q=int(input('Enter a prime number: '))
C,n,e,d=RSA_Encrypt(M,p,q)
print('Your encrypted message is: ',C)
print('Your decrypted message is: ',RSA_Decrypt(C,n,e,d))

