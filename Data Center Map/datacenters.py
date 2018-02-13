from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

with open('Data Centers.csv', 'a', newline='') as outfile:

    headers = ['Data Center', 'Company', 'Location', 'Country', 'Area']
    writer = csv.DictWriter(outfile, fieldnames=headers)
    writer.writeheader()

    with open('areas.csv', 'r') as infile:

        reader = csv.reader(infile, delimiter=',')

        for row in reader:

            url_html = urlopen(row[2]).read()
            soup = BeautifulSoup(url_html, 'html.parser')

            data_centers = soup.findAll('div', {'class': 'DCColumn1'})

            for data_center in data_centers:

                center = data_center.findAll('a')[0]
                company = data_center.findAll('a')[1]
                location = data_center.text.strip().replace(center.text,'').replace(company.text,'').replace('» Visit website','').replace('» View profile','').strip('\n')

                writer.writerow({'Data Center':center.text, 'Company':company.text, 'Location':location, 'Country':row[0], 'Area':row[1]})