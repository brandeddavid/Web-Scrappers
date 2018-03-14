from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

def getwordlist(url, filename):

    page_html = urlopen(url).read()
    soup = BeautifulSoup(page_html, 'html.parser')

    tds = soup.findAll('td', {'width': '110'})

    wordList = []

    #print(tds[5].text)

    try:

        with open(filename+'.txt', 'a', newline='\n') as outfile:

            try:

                for td in tds:

                    wordList.append(td.text)

            except:

                wordList = []
                pass

            finally:

                outfile.writelines([word + '\n' for word in wordList])
    except:

        print(filename, 'not opened')
        pass

def main():

    with open('wordlisturl.csv', 'r') as infile:

        reader = csv.reader(infile)

        for row in reader:

            getwordlist(row[1], row[0])

if __name__ == '__main__':

    main()