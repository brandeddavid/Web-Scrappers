from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

def getURLs(url):

    page_html = urlopen(url).read()
    soup = BeautifulSoup(page_html, 'html.parser')

    tds = soup.findAll('td', {'valign':'middle'})

    with open('wordlisturl.csv', 'a') as urlfile:

        writer = csv.DictWriter(urlfile, fieldnames=['Name', 'URL'])
        writer.writeheader()

        for td in tds:

            try:

                name = td.text.strip()
                url = 'https://www.spellzone.com/word_lists/' + td.a['href']

            except:

                name = ''
                url = ''
                pass

            finally:

                writer.writerow({'Name':name, 'URL':url})

if __name__ == '__main__':

    getURLs('https://www.spellzone.com/word_lists/vocabulary_lists.cfm')