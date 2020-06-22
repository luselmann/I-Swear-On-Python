 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:02:38 2020

@author: luise
"""
exclude = ('the', 'I', 'you', 'that', 'my', 'and', 'on', 'is', 'so', 'your', 'it', 'a', 'My', 'to', 'make', "I'm", 'And', 'ass,')
counts = dict() #create dict
def word_count(str):
    words = str.split()

    for word in words:
        if word not in exclude:  
            if word in counts:
                counts[word] += 1 #add value of word to dict
            else:
                counts[word] = 1 #add word to dict

def readfiles(filename): #open, read every file line by line
    fhand = open(filename)
    for line in fhand:
        word_count(line) #calls, sends to other funct
        
song_titles = ('Dancefloor.txt', 'DickByThePound.txt', 'AssNTiddies.txt') #tuple with files

for song in song_titles:
    readfiles(song) #call readfiles function

sorted_counts = sorted(counts.items(), key = lambda x: x[1], reverse = True) #sort by value/frequency, reverse it to put highest on top

print(sorted_counts)

import pyttsx3 #import text 2 speech/python package
engine = pyttsx3.init()
for swearword in range(5):
    for frequency in range(sorted_counts[swearword][1]):
        engine.say(sorted_counts[swearword][0])
    print(sorted_counts[swearword][0],sorted_counts[swearword][1],'times')
try:
    engine.runAndWait()
except:
    print("Start spyder again or I won't work!")