from bs4 import BeautifulSoup
from urllib.request import urlopen


def scrapper(url):
    """

    :param url with a list of English words/ data in its tds:
    :return: A word.txt document of words scrapped from the url tables

    """

    url_html = urlopen(url).read()

    soup = BeautifulSoup(url_html, 'html.parser')

    trs = soup.find_all('tr')

    with open('words.txt', 'a') as file:

        for tr in trs:

            # file.writelines(tr.text.strip('\n') + '\n')

            tds = tr.find_all('td')

            for td in tds:

                file.writelines(td.text.strip() + '\n')


if __name__ == '__main__':

    url = str(input('> '))

    scrapper(url)
