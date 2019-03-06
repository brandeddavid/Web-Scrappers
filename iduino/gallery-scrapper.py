from bs4 import BeautifulSoup
from urllib.request import urlopen
import wget, time, os

page = 1
base_url = 'http://www.openplatform.cc'

while page < 6:
  print('\nScraping page', page)

  try:
    url = 'http://www.openplatform.cc/index.php/Home/Index/products/aptid/6/p/' + str(page) + '.html'
    # url = 'http://www.openplatform.cc/index.php/home/index/products/aptid/4/apiinfor/'
    url_html = urlopen(url).read()
    soup = BeautifulSoup(url_html, 'html.parser')
      
    try:
      product_div = soup.findAll('div', {'class': 'searListsub'})

      for product in product_div:
        print('\nProduct ' + str(product_div.index(product)+1) + ' of ' + str(len(product_div)))

        try:
          product_title = product.findAll('h5', {'class': 'itemTitle'})[0]
          product_name = product_title.a.text
          product_url = base_url + product_title.a['href']

          try:
            product_page_html = urlopen(product_url).read()
            product_page_soup = BeautifulSoup(product_page_html, 'html.parser')
            product_carousel = product_page_soup.findAll('div', {'class': 'carousel-inner'})[0]
            product_images = product_carousel.findAll('div', {'class': 'item'})

            if len(product_images) > 1:
              os.mkdir('./' + product_name)
              for image in product_images:
                if product_images.index(image) > 0:
                  print('\nDownloading image\n', str(product_images.index(image)+1) + ' of ' + str(len(product_images)))
                  try:
                    image_url = base_url + image.a['href']
                    wget.download(image_url, './' + product_name + '/' + product_name + str(product_images.index(image)) + '.jpg')
                    time.sleep(10)
                  
                  except Exception as error:
                    print('Image download', error)
                    pass

                  finally:
                    image_url = ''
            
            else:
              print('Product', product_name, 'does not have multiple images')
              pass
          
          except Exception as error:
            print('Product page', error)
            pass

        except Exception as error:
          print('Product info', error)
          pass

        finally:
          product_name = ''
          product_url = ''
    
    except Exception as error:
      print('Product list', error)
      pass
  
  except Exception as error:
    print('Page count', error)

  finally:
    page += 1
