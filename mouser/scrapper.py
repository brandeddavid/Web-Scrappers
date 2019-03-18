from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

url = 'https://eu.mouser.com/Semiconductors/Discrete-Semiconductors/Diodes-Rectifiers/Bridge-Rectifiers/_/N-ax1mf/'

req = Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
url_html = urlopen(req).read()
soup = BeautifulSoup(url_html, 'html.parser')
table = soup.find_all('table', {'class': 'table persist-area SearchResultsTable'})
table_rows = table[0].find_all('tr')

for row in table_rows:
  try:
    manufacturer = row.find_all('td', {'class': 'column mfr-column hide-xsmall'})[0].a.text 
    print(manufacturer)

  except:
    pass
