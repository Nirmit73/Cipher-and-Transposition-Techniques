#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def encrypt_function(text, key):  
    result = ""  

    for i in range(len(text)):  
        char = text[i]  

        if (char.isupper()):  
            result += chr((ord(char) + key - 65) % 26 + 65)  

        else:  
            result += chr((ord(char) + key - 97) % 26 + 97)  
    return result
def decrypt_function(var, key):  
    pt = ""  

    for i in range(len(var)):  
        char = var[i]  

        if (char.isupper()):  
            pt += chr((ord(char) - key - 65) % 26 + 65)  

        else:  
            pt += chr((ord(char) - key - 97) % 26 + 97)  
    return pt
  
text=input('Enter plain text: ')
key=int(input('Key: '))
encrypt=encrypt_function(text, key)
decrypt=decrypt_function(encrypt, key)
print('Your ciphered text is:',encrypt)
print('Your deciphered text is:',decrypt)

