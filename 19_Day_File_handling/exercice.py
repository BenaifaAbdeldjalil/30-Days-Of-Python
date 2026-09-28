# -*- coding: utf-8 -*-
#Exercises: Level 1
from pathlib import Path

base = "/data/"
file_obama = "obama_speech.txt"
file = Path("data/obama_speech.txt")

with  file.open('r' , encoding="utf-8") as f :
    lines = f.readlines()
    content = f.read()# mode(r, a, w, x, t,b)
    words=content.split(" ")
    print(f'extrait : {words}')
    #lines = f.readlines()
with  file.open('r' , encoding="utf-8") as f :
    content = f.read()# mode(r, a, w, x, t,b)
    words=content.split()

print(len(content),content) #caractere
print(len(words),words) #words
print(len(lines)) #lignes


#Read obama_speech.txt file and count number of lines and words
#Read michelle_obama_speech.txt file and count number of lines and words
#Read donald_speech.txt file and count number of lines and words
#Read melina_trump_speech.txt file and count number of lines and w
