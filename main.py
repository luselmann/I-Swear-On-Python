import pyttsx3 #import text 2 speech/python package
from request import getlyrics #referrs to other document -> getlyrics function

engine = pyttsx3.init() #initializing speech engine
exclude = ('the', 'i', 'you', 'that', 'my', 'and', 'on', 'is', 'so', 'your', 'it', 'a', 'to', 'make', "i'm")
# tuple of words to exclude
counts = dict() #create dict

file = getlyrics(input('Enter song and artist: ')) #returned lyrics from getlyrics funtion defined as file
perfectwords = file.lower().replace('.', '').replace(',', '').replace('\n', ' ').replace('-', '').split()
#all words in file made lowercase, fullstops + commas + paragraph + hyphens removed and split string lines to single words

for word in perfectwords: #all perfectwords run through for loop
    if word not in exclude:
        if word in counts:
            counts[word] += 1 #add value of word to dict -> word already occured
        else:
            counts[word] = 1 #add word to dict -> new word

sorted_counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)
#sort by value/frequency, reverse it to put highest on top

firstfive = dict(sorted_counts[:5]) #five most occured words in lyrics
print(firstfive)

for word in perfectwords:
    if word in firstfive:
        print(word)
        engine.say(word) #text to speech

engine.runAndWait() #command for engine to start
