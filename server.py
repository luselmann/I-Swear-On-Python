from flask import Flask, request
from flask_cors import CORS, cross_origin
from lyrics import getlyrics
from sortwords import sortwords

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST', 'GET'])
@cross_origin()

def final():
    name = request.get_json()['name']
    lyrics = getlyrics(name)

    sortedwords = sortwords(lyrics.get('lyrics'))

    finishedwords = []

    for word in lyrics.get('lyrics').split():
        if word in sortedwords:
            finishedwords.append(word)

    return {
        'lyrics': finishedwords,
        'title': lyrics.get('full_title')
    }
