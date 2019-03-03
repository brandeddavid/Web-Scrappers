from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv, wget, time

base_url = 'http://www.openplatform.cc'
page = 1

with open('iduino-board.csv', 'a', newline='') as file:
  headers = ['Name', 'Number', 'Image', 'Page', 'Description']
  writer = csv.DictWriter(file, fieldnames=headers)
  writer.writeheader()

  while page < 12:
    print('\nScraping page', page)

    try:
      url = 'http://www.openplatform.cc/index.php/Home/Index/products/aptid/7/p/' + str(page) + '.html'
      # url = 'http://www.openplatform.cc/index.php/home/index/products/aptid/26/apiinfor/'
      url_html = urlopen(url).read()
      soup = BeautifulSoup(url_html, 'html.parser')
        
      try:
        product_div = soup.findAll('div', {'class': 'searListsub'})

        for product in product_div:
          print('\nProduct ' + str(product_div.index(product)+1) + ' of ' + str(len(product_div)))

          try:
            product_name = product.findAll('h5', {'class': 'itemTitle'})[0].a.text
            product_no = product.findAll('div', {'class': 'c9'})[0].text
            product_image = base_url + product.findAll('img', {'class': 'img-responsive'})[0]['src']
            wget.download(product_image, './' + product_name + '.jpg')
            time.sleep(5)
            product_url = base_url + product.findAll('a', {'class': 'thumb'})[0]['href']

            try:
              product_page_html = urlopen(product_url).read()
              product_page_soup = BeautifulSoup(product_page_html, 'html.parser')
              product_description = product_page_soup.findAll('div', {'class': 'editBox'})[0].text
            
            except Exception as error:
              print('Product page', error)
              pass

          except Exception as error:
            print('Product info', error)
            pass

          finally:
             writer.writerow({'Name': product_name, 'Number': product_no, 'Image': product_image, 'Page': product_url, 'Description': product_description})
            product_name = ''
            product_no = ''
            product_image = ''
            product_url = ''
            product_description = ''
      
      except Exception as error:
        print('Product list', error)
        pass
    
    except Exception as error:
      print('Page count', error)

    finally:
      page += 1
