from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os, csv, wget, time

base_url = 'https://www.digikey.com'
url = 'https://www.digikey.com/products/en/audio-products/accessories/159'
url_html = urlopen(url).read()
soup = BeautifulSoup(url_html, 'html.parser')
table = soup.find_all('tbody', {'id': 'lnkPart'})
table_rows = table[0].find_all('tr')

for row in table_rows:
  print('Scraping row {} of {}'.format(table_rows.index(row)+1, len(table_rows)))

  try:
    description = row.find_all('td', {'class': 'tr-description'})[0].text.strip()
    os.mkdir('./' + description)
    time.sleep(1)
    manufacturer = row.find_all('td', {'class': 'tr-vendor'})[0].span.a.span.text.strip()
    datasheet_url = row.find_all('a', {'class': 'lnkDatasheet'})[0]['href']
    wget.download(datasheet_url, './{}/'.format(description))
    time.sleep(5)
    product_url = base_url + row.find_all('td', {'class': 'tr-image'})[0].a['href']

    try:
      req = Request(
          product_url, 
          data=None, 
          headers={
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
          }
      )
      product_url_html = urlopen(req).read()
      product_url_soup = BeautifulSoup(product_url_html, 'html.parser')
      image_url = 'https:' + product_url_soup.find_all('a', {'class': 'product-photo-large'})[0]['href']
      print(image_url)
      wget.download(image_url, './{}/'.format(description))
    
    except Exception as error:
      print('\nImage download error', error)

    finally:
      product_url_html = ''
      image_url = ''

    with open('./{}/product.csv'.format(description), 'a', newline='') as file:
      headers = ['Manufacturer', 'Description']
      writer = csv.DictWriter(file, fieldnames=headers)
      writer.writeheader()
      writer.writerow({ 'Manufacturer': manufacturer, 'Description':description })
    
  except Exception as error:
    print('\nGet row data error', error)

  finally:
    description = ''
    manufacturer = ''
    datasheet_url = ''
    product_url = ''
