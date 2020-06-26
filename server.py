from flask import Flask, request #import flask server
from flask_cors import CORS, cross_origin #import to resolve cors error
from lyrics import getlyrics
from sortwords import sortwords

app = Flask(__name__) #start flask(configured from tutorial)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST', 'GET']) #defining routes with slash
@cross_origin() #part of cors

def final():
    name = request.get_json()['name'] #asks for title/song
    lyrics = getlyrics(name) #gets lyrics by entered song

    sortedwords = sortwords(lyrics.get('lyrics')) #gives back top 5 words

    finishedwords = [] #start empty list

    for word in lyrics.get('lyrics').split():
        if word in sortedwords:
            finishedwords.append(word) #if word in top 5, add to list

    return {
        'lyrics': finishedwords,
        'title': lyrics.get('full_title')
    }
