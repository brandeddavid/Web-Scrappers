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

with open('words.txt', 'a') as file:

    for word in words:

        file.writelines(str(word.text.strip().encode('ascii', 'ignore').decode()) + '\n')
