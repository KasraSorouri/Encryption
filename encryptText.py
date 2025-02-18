import pandas as pd
import numpy as np

with open ('uncode.txt','r') as file:
    myText = file.read()
    
# print (myText)
txtSt1 = myText.split()
# print (txtSt1)

## Generating random code
code1 = np.random.randint(0, 100* len(txtSt1), len(txtSt1))
code1.sort()
code1

## Covert Code to String
code2=[]
for s in code1:
    code2.append(str(s))
code2

## Merge words and Codes and make a coded words
cw = []
wn = 0
for w in txtSt1:
    c = code2[wn]
    s = min(len(w),len(code2[wn]))  ## Miximum Possible Slice
#    print (f' w : {w} ({len(w)}) , code: {code2[wn]} ({len(code2[wn])}) , s: {s}')
    s1 = np.random.randint(0,s) ## Slice per Word
    txt_s1 = np.linspace(0,len(w),s1+1)
    code_s1 = np.linspace(0, len(code2[wn]), s1+1) ## Slice per Code
#    print(f' w: {w} , s1: {s1} , txt_s1: {txt_s1} , code_s1: {code_s1}  ' )
    s2 = int(s1)
    ws1 = 0 ## Start Character of Word Slice
    cs1 = 0 ## Start Character of Code Slice
    i = 0
    w3 = ''
    
    
    while s2 >= 0:
        ws2 = int(txt_s1[i])+1 ## End Character of Word Slice
        cs2 = int(code_s1[i])+1 ## End Character of Code Slice
#        print(f's2: {s2}, ws1: {ws1} , ws2: {ws2} , cs2: {cs2} ')
        ws = w[ws1:ws2] ## Word Slice
        if ( cs2 > len(c) ):
            cs = c[cs1:]
        else:
            cs = c[cs1:cs2] ## Code Slice
#        print(' ** ws :  ',ws  , ' ** cs: ', cs)
        w3 = w3 + ws + cs 
        ws1 = ws2
        cs1 = cs2
        s2 -=1
        i +=1
    w3 = w3 + w[ws2:] + c[cs2:]+ '$'
#    print ('w3 = ',w3)
    wn +=1
#    print ('******* cw : ', cw)
    cw.append(w3)
#    print ('******* cw2 : ', cw)

## Shuffle words
np.random.shuffle(cw)
cw

## Make Final Text
ct = ''
for item in cw:
    ct = ct + item
print ('**** ct : ',ct)

## Write final text to file

with open ('encryptedText.txt','w') as file:
    file.write(ct)
