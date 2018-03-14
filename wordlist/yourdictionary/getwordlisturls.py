from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

def getLink(url):

    page_html = urlopen(url).read()

    soup = BeautifulSoup(page_html, 'html.parser')

    divs = soup.findAll('div', {'class':'twelve'})

    with open ('links.csv', 'a') as linkfile:

        writer = csv.DictWriter(linkfile, fieldnames=['Name', 'URL'])
        writer.writeheader()

        for div in divs:

            try:

                link = div.h4.a['href'].strip()
                name = div.text.strip()

            except:

                link = ''
                name = ''
                pass

            finally:

                writer.writerow({'Name':name, 'URL':link})

if __name__ == '__main__':

    getLink('http://grammar.yourdictionary.com/word-lists/')