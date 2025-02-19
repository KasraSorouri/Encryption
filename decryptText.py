import pandas as pd
import numpy as np
import re

with open ('encryptedText.txt', 'r') as file:
    myText = file.read()


ewl = myText.split('$') ## male a list of encrypted words
 
## Make a dic based on words and their positions
wl = {}
for item in ewl:
    if (item != ''):
        word = re.sub(r'[^a-zA-Z\'.,]', '', item)  # Remove all non-alphabetic characters
        code = re.sub(r'[^0-9]', '', item)     # Remove all non-numeric characters
        print (f' w: {word}  ,  code :  {code}  ')
        wl[word] = int(code)

print ('** wl :' ,wl)

swl = dict(sorted(wl.items(), key=lambda item: item[1])) ## Sort words based on their position
print ('** wl2 :' ,wl)
print ('** swl :' ,swl)

## extract the Original text
txt = ''
for item in swl:
    txt = txt + item + ' '
print ('txt   : ',txt)