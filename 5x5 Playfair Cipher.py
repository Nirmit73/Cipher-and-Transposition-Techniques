#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def makeMatrix(a):
    a = a.replace(" ","")
    tempList = []
    string = ""
    for i in a:
        if i not in tempList:
            tempList.append(i)
            string+=i
    table = [["" for j in range(0,5)] for i in range(0,5)]
    i = 0
    j = 0
    alphabets = 0
    for k in range(0,len(string)):
            if j > 4:
                j = 0
                i+=1
            table[i][j] = string[k]
            j+=1
            
    while i != 4 or j != 5:
        if j > 4:
            j = 0
            i+=1
        if chr(65+alphabets) not in string and chr(65+alphabets) != "J":
            table[i][j] = chr(65+alphabets)
            j+=1
        alphabets+=1
    return table

def divideTheWord(a):
    string = ""
    a = a.replace(" ","")
    i = 0
    while i < (len(a)):
        try:
            if a[i] != a[i+1]:
                string+=f"{a[i]+a[i+1]} "
                i+=2
            else:
                string+=f"{a[i]}X "
                i+=1
        except:
                string+=f"{a[i]}X "
                i+=1
    return string.split()

def findRowAndIndex(a,matrix):
    if a == "J": a = "I"
    for i in range(0,5):
        for j in range(0,5):
            if matrix[i][j] == a :
                    return i,j

def playFairEncryption(table,dividedPlainWord):
    dividedEncryptedWord = []
    for i in dividedPlainWord:
        firstRow,firstIndex = findRowAndIndex(i[0],table)
        secondRow,secondIndex = findRowAndIndex(i[1],table)
        if firstRow == secondRow:
            first = table[firstRow][0] if firstIndex+1 > 4 else table[firstRow][firstIndex+1]
            second = table[secondRow][0] if secondIndex+1 > 4 else table[secondRow][secondIndex+1]
            dividedEncryptedWord.append(first+second)
        elif firstIndex == secondIndex:
            first = table[0][firstIndex] if firstRow+1 > 4 else table[firstRow+1][firstIndex]
            second = table[0][secondIndex] if secondRow+1 > 4 else table[secondRow+1][secondIndex]
            dividedEncryptedWord.append(first+second)
        else:
            first,second =table[firstRow][secondIndex],table[secondRow][firstIndex]
            dividedEncryptedWord.append(first+second)
    return dividedEncryptedWord

def playFairDecryption(table,dividedEncryptedWord):
    dividedDecryptedWord = []
    for i in dividedEncryptedWord:
        firstRow,firstIndex = findRowAndIndex(i[0],table)
        secondRow,secondIndex = findRowAndIndex(i[1],table)
        if firstRow == secondRow:
            first = table[firstRow][-1] if firstIndex-1 < 0 else table[firstRow][firstIndex-1]
            second = table[secondRow][-1] if secondIndex-1 < 0 else table[secondRow][secondIndex-1]
            dividedDecryptedWord.append(first+second)
        elif firstIndex == secondIndex:
            first = table[-1][firstIndex] if firstRow-1 < 0 else table[firstRow-1][firstIndex]
            second = table[-1][secondIndex] if secondRow-1 < 0 else table[secondRow-1][secondIndex]
            dividedDecryptedWord.append(first+second)
        else:
            first,second =table[firstRow][secondIndex],table[secondRow][firstIndex]
            dividedDecryptedWord.append(first+second)
    return dividedDecryptedWord

sentence = input("Enter the plain text: ")
key = input("Enter the key: ")
table = makeMatrix(key.upper())
dividedPlainWord = divideTheWord(sentence.upper())
for i in table:
    print(i)
print()

dividedEncryptedWord = playFairEncryption(table,dividedPlainWord)
print("Encrypted Words: "+" ".join(dividedEncryptedWord))

dividedDecryptedWord = playFairDecryption(table,dividedEncryptedWord)
print("Decrypted Words: "+" ".join(dividedDecryptedWord))

print("Decrypted text: "+"".join(dividedDecryptedWord).replace("X",""))

