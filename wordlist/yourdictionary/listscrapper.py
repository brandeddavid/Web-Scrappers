from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#url = 'http://grammar.yourdictionary.com/word-lists/More-About-Words-That-End-in-Q.html'

def scrapper(url):

    """

    :param url:
    :return: word.txt document with all list data within the url

    """


    url_html = urlopen(url).read()

    soup = BeautifulSoup(url_html, 'html.parser')

    wordsContainer = soup.findAll('div', {'id':'article_main_content'})

    words = wordsContainer[0].findAll('li')


    with open('words.txt', 'a') as file:

        for word in words:

            file.writelines(str(word.text.strip().encode('ascii', 'ignore').decode()) + '\n')

if __name__ == '__main__':

    while True:

        url = str(input('> '))
        scrapper(url)
