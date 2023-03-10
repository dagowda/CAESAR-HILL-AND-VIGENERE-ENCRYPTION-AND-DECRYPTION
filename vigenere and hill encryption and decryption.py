import numpy as np
str1=""
str2=""
def ver_str_enc(planetext,key):
    global str1
    key=key.lower()
    d=0
    planetext=planetext.replace(' ','')
    if len(planetext)!= len(key):
        for g in range(len(key), len(planetext)):
            key=key+key[d]
            d+=1
    ciphertxt=""
    planetext = planetext.lower()
    a=int(len(planetext))
    b=int(len(key))
    for i in range(0, a):
     for j in range(0 ,1):
        c=ord(planetext[i])
        d=ord(key[i])
        caesar_str_enc(c,d)
    print("encrypted cipher :" +str1.upper())
def caesar_str_enc(n,m):
    global str1
    count=0
    n=n-97
    key=m-97
    for i in range(0, key):
        count=count+1
    str=chr(((n+count)%26)+97)
    str1=str1+str
def ver_str_dec(enctxt,key):
    global str2
    key=key.lower()
    d = 0
    enctxt = enctxt.replace(' ', '')
    if len(enctxt) != len(key):
        for g in range(len(key), len(enctxt)):
            key = key + key[d]
            d += 1
    planetxt=""
    enctxt = enctxt.lower()
    a=int(len(enctxt))
    b=int(len(key))
    for i in range(0, a):
      for j in range(0 ,1):
        l=ord(enctxt[i])
        w=ord(key[i])
        caesar_str_dec(l,w)
    print("decrypted cipher :" +str2.upper())
def caesar_str_dec(n,m):
    global str2
    count = 0
    n = n - 97
    key = m - 97
    for i in range(0, key):
        count = count + 1
    strr = chr(((n - count) % 26) + 97)
    str2 = str2 + strr
def hill_enc(m,n):
    f=[]
    m=m.replace(' ','')
    asclist = [ord(c.upper()) - 65 for c in m if c.isalpha()]
    sublist = [asclist[i:i + 3] for i in range(0, len(asclist), 3)]
    l=len(sublist)
    a=len(sublist[l-1])
    if a != 3:
        for i in range(a ,3):
            sublist[l-1].append(88)
    print(sublist)

    for i in range(0, l):
        c=np.matmul(sublist[i],n)%26
        letters= [chr(a+65) for a in c]
        print(letters)
        f=f+letters
    s=''.join(f)
    print("the encrypted hill cypher is:" +s.upper())



v=str(input("please enter the text to encrypt :"))
z=str(input("please enter the text to decrypt :"))
x=str(input("please enter the key :"))
a=str(input("please enter the string to encrypt using hill encryption :"))
ver_str_enc(v,x)
ver_str_dec(z,x)
d = np.array([[17,17,5],[21,18,21],[2,2,19]])
hill_enc(a,d)


