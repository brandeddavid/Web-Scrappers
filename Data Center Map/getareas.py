from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

with open('countriesbk.csv', 'r') as file:

    reader = csv.reader(file, delimiter=',')

    for row in reader:

        url_html = urlopen(row[1]).read()
        soup = BeautifulSoup(url_html, 'html.parser')

        column1 = soup.findAll('div', {'class': 'column1'})
        column2 = soup.findAll('div', {'class': 'column2'})
        column3 = soup.findAll('div', {'class': 'column3'})

        with open('areas2.csv', 'a', newline='') as outfile:

            headers = ['Country', 'Area', 'URL']

            writer = csv.DictWriter(outfile, fieldnames=headers)
            #writer.writeheader()

            if len(column1) == 0:

                pass

            else:

                for link in column1[0].findAll('a'):

                    writer.writerow({'Country':row[0], 'Area':link.text, 'URL':'http://www.datacentermap.com'+link['href']})
            if len(column2) == 0:

                pass

            else:

                for link in column2[0].findAll('a'):
                    writer.writerow({'Country': row[0], 'Area': link.text, 'URL': 'http://www.datacentermap.com' + link['href']})

            if len(column3) == 0:

                pass

            else:

                for link in column3[0].findAll('a'):
                    writer.writerow({'Country': row[0], 'Area': link.text, 'URL': 'http://www.datacentermap.com' + link['href']})
