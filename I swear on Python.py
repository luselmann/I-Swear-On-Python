 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:02:38 2020

@author: luise
"""

import pyttsx3 #import text 2 speech/python package
engine = pyttsx3.init()

exclude = ('the', 'i', 'you', 'that', 'my', 'and', 'on', 'is', 'so', 'your', 'it', 'a', 'to', 'make', "i'm")
counts = dict() #create dict
file = ()

def word_count(str):
    str = str.lower()
    str = str.replace(',', '')
    str = str.replace('.', '')
    words = str.split()

    for word in words:
        if word not in exclude:
            if word in counts:
                counts[word] += 1 #add value of word to dict
            else:
                counts[word] = 1 #add word to dict

file = open('AssNTiddies.txt')
for line in file:
    word_count(line)

sorted_counts = sorted(counts.items(), key = lambda x: x[1], reverse = True) #sort by value/frequency, reverse it to put highest on top

firstfive = dict(sorted_counts[:5])
print(firstfive)

print(file)

for line in open('AssNTiddies.txt'):
    for word in line.split():
        word = word.lower().replace('.', '').replace(',', '')
        if word in firstfive:
            print(word)
            engine.say(word)

try:
    engine.runAndWait()
except:
    print("Start spyder again or I won't work!")
