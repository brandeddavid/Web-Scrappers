from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

url = 'http://www.datacentermap.com/datacenters.html'
url_html = urlopen(url).read()
soup = BeautifulSoup(url_html, 'html.parser')

column1 = soup.findAll('div', {'class':'column1'})
column2 = soup.findAll('div', {'class':'column2'})
column3 = soup.findAll('div', {'class':'column3'})

with open('countries.csv', 'a', newline='') as file:

    headers = ['Name', 'URL']
    writer = csv.DictWriter(file, fieldnames=headers)
    #writer.writeheader()

    for link in column1[0].findAll('a'):

        writer.writerow({'Name':link.text, 'URL':'http://www.datacentermap.com'+link['href']})

    for link in column2[0].findAll('a'):

        writer.writerow({'Name':link.text, 'URL':'http://www.datacentermap.com'+link['href']})

    for link in column3[0].findAll('a'):

        writer.writerow({'Name':link.text, 'URL':'http://www.datacentermap.com'+link['href']})