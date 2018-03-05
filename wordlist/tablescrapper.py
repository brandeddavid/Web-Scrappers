from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://www.enchantedlearning.com/wordlist/animal.shtml'

url_html = urlopen(url).read()

soup = BeautifulSoup(url_html, 'html.parser')

trs = soup.find_all('tr')

wordList = []

with open('words.txt', 'a') as file:

    for tr in trs:

        tds = tr.find_all('td')

        for td in tds:

            file.writelines(td.text.strip() + '\n')
