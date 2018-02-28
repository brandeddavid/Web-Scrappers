from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url = 'http://grammar.yourdictionary.com/for-students-and-parents/words-with-multiple-meanings.html'

url_html = urlopen(url).read()

soup = BeautifulSoup(url_html, 'html.parser')

wordsContainer = soup.findAll('div', {'id':'article_main_content'})

words = wordsContainer[0].findAll('li')

wordList = []

pattern = "[\-\:]"

for word in words:

    #wordList.append(word.text.strip())

    wordList.append(re.split(pattern, word.text)[0].strip())

print(wordList)