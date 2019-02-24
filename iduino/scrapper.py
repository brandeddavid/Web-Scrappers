from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv, wget

url = 'http://www.openplatform.cc/index.php/home/index/products'
url_html = urlopen(url).read()
soup = BeautifulSoup(url_html, 'html.parser')

with open('products.csv', 'a', newline='') as file:
  headers = ['Name', 'Number', 'Image']
  writer = csv.DictWriter(file, fieldnames=headers)
  writer.writeheader()
  
  try:
    product_div = soup.findAll('div', {'class': 'searListsub'})

    for product in product_div:
      try:
        product_name = product.findAll('h5', {'class': 'itemTitle'})[0].a.text
        product_no = product.findAll('div', {'class': 'c9'})[0].text
        product_image = 'http://www.openplatform.cc' + product.findAll('img', {'class': 'img-responsive'})[0]['src']
        wget.download(product_image, './' + product_name + '.jpg')

      except Exception as e:
        print(e)

      finally:
        writer.writerow({'Name': product_name, 'Number': product_no, 'Image': product_image})
  
  except Exception as error:
    print(error)
