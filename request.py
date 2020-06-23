import requests #tool to request info from website
import json #import to adjust to block format -> easy to read
from bs4 import BeautifulSoup #tool to find div(lyrics element) in html/interact with html

#FUNCTIONS

def printJSON(s):
    print(json.dumps(s, indent = 4, sort_keys = True, ensure_ascii = False))
    #print JSON format in alphabetical order and let apostrophes be used

def getlyrics(song):
    headers = { 'Authorization': 'Bearer C0eD8lJNIEd7F6z4-5vW-7yYbV_PCcPBGDjluLChqg5BM-hP2x7vjg2ljBhCiYeg' }
    #authorization for genius api

    data = { 'q': song } #song data entered and searched for

    response = requests.get('https://api.genius.com/search', data = data, headers = headers).json()
    #request for song results from genius api in JSON

    hits = response['response']['hits'] #definition of hits for following conditional etc.

    if len(hits) < 1:
        return 'no songs found' #if less than 1(none) hit found -> no songs found

    result = hits[0]['result'] #first result chosen automatically (taken from result JSON block)

    url = result['url'] #defines url for first result (taken from url JSON block)
    full_title = result['full_title'] #defines title and artist (taken from full_title JSON block)
    printJSON(full_title) #prints title and artist in JSON format

    page = requests.get(url) #finds page/url of song

    html = BeautifulSoup(page.text, 'html.parser') #finds elements in html

    div = html.find('div', { 'class': 'lyrics' }) #finds lyrics element

    if div is None:
        return 'no lyrics found' #if no lyrics available for the song -> no lyrics found

    lyrics = div.get_text() #defines lyrics as text taken from correct div -> gets only text from div

    return lyrics #returns and displays lyrics
