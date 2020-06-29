import pyttsx3 #import text 2 speech/python package
from lyrics import getlyrics #referrs to other document -> getlyrics function
from sortwords import sortwords

engine = pyttsx3.init() #initializing speech engine

file = getlyrics(input('Enter song and artist: ')) #returned lyrics from getlyrics funtion defined as file
lyrics = file.get('lyrics')
firstfive = sortwords(lyrics)

print(lyrics.split())

for word in lyrics.split(): #split line into words
    if word in firstfive:
        print(word) #print top 5 words
        engine.say(word) #text to speech

engine.runAndWait() #command for engine to start
