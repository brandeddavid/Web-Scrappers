from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import time

links = []

with open('links20.csv', 'r') as file:

    reader = csv.reader(file, delimiter=',')

    for row in reader:

        links.append(row[0])

with open('speakers.csv', 'a', newline='') as tofile:

    headers = ['Name', 'Details', 'Description']
    writer = csv.DictWriter(tofile, fieldnames=headers)

    writer.writeheader()

    try:

        for url in links:

            print ('Scrapping:', links.index(url)+1, 'of', len(links))

            try:

                url_html = urlopen(url).read()
                soup = BeautifulSoup(url_html, 'html.parser')
                speaker = soup.findAll('h1', {"class": "orange"})
                name = speaker[0].text
                description_div = soup.findAll('div', {'class': 'description'})
                description = description_div[0].text.strip()

                details = soup.findAll('div', {'class': 'grey'})

                deets = ''

                for item in details:

                    if details.index(item)>4:

                        pass

                    else:

                        deets += item.text + '\n'

                writer.writerow({'Name': name, 'Details': deets, 'Description':description})
                print('Done with:', links.index(url) + 1, 'of', len(links))

            except:

                pass

            finally:

                deets = ''
                description_div = []
                time.sleep(1)

    except:

        pass

