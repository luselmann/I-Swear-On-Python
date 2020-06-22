import pyttsx3 #import text 2 speech/python package

engine = pyttsx3.init()
exclude = ('the', 'i', 'you', 'that', 'my', 'and', 'on', 'is', 'so', 'your', 'it', 'a', 'to', 'make', "i'm")
counts = dict() #create dict

# FUNCTIONS

def word_count(words):
    for word in words:
        if word not in exclude:
            if word in counts:
                counts[word] += 1 #add value of word to dict
            else:
                counts[word] = 1 #add word to dict

# PROGRAM START

file = open('AssNTiddies.txt').read()
perfectwords = file.lower().replace('.', '').replace(',', '').replace('\n', ' ').split()

word_count(perfectwords)

sorted_counts = sorted(counts.items(), key = lambda x: x[1], reverse = True) #sort by value/frequency, reverse it to put highest on top

firstfive = dict(sorted_counts[:5])
print(firstfive)

for word in perfectwords:
    if word in firstfive:
        print(word)
        engine.say(word)

engine.runAndWait()
