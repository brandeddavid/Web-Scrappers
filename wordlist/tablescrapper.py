from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://grammar.yourdictionary.com/parts-of-speech/adjectives/List-of-Descriptive-Adjectives.html'

url_html = urlopen(url).read()

soup = BeautifulSoup(url_html, 'html.parser')

trs = soup.find_all('tr')

wordList = []

for tr in trs:

    tds = tr.find_all('td')

    for td in tds:

        wordList.append(td.text.strip())

print(wordList)