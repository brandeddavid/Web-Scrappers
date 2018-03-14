from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://grammar.yourdictionary.com/word-lists/government-accounting-terms.html'

url_html = urlopen(url).read()

soup = BeautifulSoup(url_html, 'html.parser')

wordsContainer = soup.findAll('h3')

with open('words.txt', 'w') as file:

    for word in wordsContainer:

        file.writelines(word.text + '\n')