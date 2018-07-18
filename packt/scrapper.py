import requests, csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

with open('authors.csv', 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Description', 'URL'])
    writer.writeheader()
    offset = 0
    while offset < 4800:
        try:
            url = 'https://www.packtpub.com/books/info/packt/authors?search_box=&offset='+str(offset)+'&rows=48&alphabet='
            page_html = urlopen(url).read()
            soup = BeautifulSoup(page_html, 'html.parser')
            authors = soup.findAll("div", {"class":"packt-author-line-view"})
            for author in authors:
                try:
                    print("Offset", offset, "Author", authors.index(author)+1, "of", len(authors))
                    name = author.div.h3.text
                    description = author.findAll("div", {"class": "packt-author-line-view-description"})[0].text.strip()
                    detail_url = "https://www.packtpub.com" + author.findAll("div", {"class": "packt-author-line-view-detail-link"})[0].a["href"]
                    writer.writerow({"Name": name, "Description": description, "URL": detail_url})
                except Exception as e:
                    print(e)
                    pass
                finally:
                    name = ''
                    description = ''
                    detail_url = ''
        except Exception as e:
            print(e)
            pass
        finally:
            offset += 48
