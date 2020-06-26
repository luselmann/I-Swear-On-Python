import pyttsx3 #import text 2 speech/python package
from lyrics import getlyrics #referrs to other document -> getlyrics function
from sortwords import sortwords

engine = pyttsx3.init() #initializing speech engine

file = getlyrics(input('Enter song and artist: ')) #returned lyrics from getlyrics funtion defined as file
lyrics = file.get('lyrics')
firstfive = sortwords(lyrics)

print(lyrics.split())

for word in lyrics.split():
    if word in firstfive:
        print(word)
        engine.say(word) #text to speech

engine.runAndWait() #command for engine to start
