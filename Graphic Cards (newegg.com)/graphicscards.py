from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

#url to scrape
url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#
url_html = urlopen(url).read()

#html parsing with BeautifulSoup
soup =BeautifulSoup(url_html, 'html.parser')

#finds all item-container classes (holds graphic card details)
graphiccards = soup.findAll("div", {"class":"item-container"})

with open ('graphiccards.csv', 'w', newline = '') as file:

    headers = ['Brand', 'Name', 'Price', 'Shipping']

    writer = csv.DictWriter(file, fieldnames=headers)

    writer.writeheader()

    for card in graphiccards:

        try:
            #Traverse to find the card's brand title
            brand = card.div.div.a.img['title']

            #Finds container housing card name
            #Returns a list of all containers
            name_container = card.findAll("a", {"class":'item-title'})

            #List returned has one entry of container with card name
            #Grab text from the first item in list
            name = name_container[0].text

            #Finds li housing card price
            #Returns a list of all li
            price_li = card.findAll('li', {'class':'price-current'})

            #List returned has one entry of li with card price
            #Grab text from the first item in list
            price = price_li[0].text.strip()

            #Finds li housing card shipping details
            #Returns a list of all li
            shipping_li = card.findAll('li', {'class':'price-ship'})

            #List returned has one entry of li with card shipping details
            #Grab text from the first item in list
            shipping = shipping_li[0].text.strip()

            writer.writerow({'Brand':brand, 'Name':name, 'Price':price, 'Shipping':shipping})

        except:

            pass
