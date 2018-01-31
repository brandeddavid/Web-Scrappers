from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import csv
import time

browser = webdriver.Firefox()

cities =  []

url = 'https://www.electricitylocal.com/states/arkansas//'

browser.get(url)
time.sleep(1)

dropdown = browser.find_element_by_xpath('//*[@id="city"]')

for city in dropdown.text.split('\n'):

    cities.append(city)


browser.close()

for city in cities:

    print('Scraping: ', city)

    try:

        url = 'https://www.electricitylocal.com/states/arkansas/' + city.lower().replace(' ', '-') + '/'

        with open('arkansas.csv', 'a', newline='') as file:

            headers = ['City', 'Commercial', 'Residential', 'Industrial']

            writer = csv.DictWriter(file, fieldnames=headers)

            try:

                url_html = urlopen(url).read()
                soup = BeautifulSoup(url_html,'html.parser')
                rates_div = soup.findAll('div', {'id':'info-container'})
                rates = rates_div[0].findAll('ul', {'class':'no2'})

                commercial = rates[0].li.strong.text
                residential = rates[1].li.strong.text
                industrial = rates[2].li.strong.text

            except:

                pass

            finally:

                writer.writerow({'City':city, 'Commercial':commercial, 'Residential':residential, 'Industrial':industrial})

    except:

        pass



