from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'https://www.digikey.com/products/en/discrete-semiconductor-products/diodes-bridge-rectifiers/299'
url_html = urlopen(url).read()
soup = BeautifulSoup(url_html, 'html.parser')
table = soup.find_all('table', {'id': 'productTable'})
table_rows = table[0].find_all('tr')

for row in table_rows:
  try:
    manufacturer = row.find_all('td', {'class': 'tr-vendor'})[0].span.a.span.text
    print(manufacturer)
    
  except Exception as error:
    print(error)