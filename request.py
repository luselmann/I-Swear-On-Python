import requests
import json
from bs4 import BeautifulSoup

def printJSON(s):
    print(json.dumps(s, indent = 4, sort_keys = True, ensure_ascii = False))

def getlyrics(song):
    headers = { 'Authorization': 'Bearer C0eD8lJNIEd7F6z4-5vW-7yYbV_PCcPBGDjluLChqg5BM-hP2x7vjg2ljBhCiYeg' }

    data = { 'q': song }

    response = requests.get('https://api.genius.com/search', data = data, headers = headers).json()

    result = response['response']['hits'][0]['result']

    url = result['url']
    full_title = result['full_title']
    printJSON(full_title)

    page = requests.get(url)

    html = BeautifulSoup(page.text, 'html.parser')

    lyrics = html.find('div', class_='lyrics').get_text()
    return lyrics
