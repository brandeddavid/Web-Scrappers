from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://grammar.yourdictionary.com/parts-of-speech/adjectives/list-of-adjectives-to-describe-tone-feelings-emotions.html'

url_html = urlopen(url).read()

soup = BeautifulSoup(url_html, 'html.parser')

wordsContainer = soup.findAll('tr')

words = wordsContainer.findAll('td')

wordList = []

for word in words:

    wordList.append(word.text.strip())

print(wordList)