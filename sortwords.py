def sortwords(words):
    exclude = ('in', 'the', 'i', 'you', 'that', 'my', 'and', 'on', 'is', 'so', 'your', 'it', 'a', 'to', 'make', "i'm")
    # tuple of words to exclude

    perfectwords = words.split()
    counts = dict() #create dict

    for word in perfectwords: #all perfectwords run through for loop
        if word not in exclude:
            if word in counts:
                counts[word] += 1 #add value of word to dict -> word already occured
            else:
                counts[word] = 1 #add word to dict -> new word

    sorted_counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)
    #sort by value/frequency, reverse it to put highest on top

    firstfive = dict(sorted_counts[:5]) #five most occured words in lyrics

    return firstfive
