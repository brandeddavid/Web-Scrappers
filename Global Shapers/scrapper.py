from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

page = 1

while page < 35:

    print ('Scraping page', page)

    try:

        url = 'https://www.globalshapers.org/alumni?page=' + str(page)


        url_html = urlopen(url).read()

        soup =BeautifulSoup(url_html, 'html.parser')

        people_div = soup.findAll("div", {"class":"hub__person"})


        with open ('alumini.csv', 'a', newline = '') as file:

            headers = ['Name', 'Position', 'Company', 'Twitter', 'LinkedIn', 'Facebook']

            writer = csv.DictWriter(file, fieldnames=headers)

            #writer.writeheader()

            for person in people_div:

                try:

                    name_class = person.findAll('div', {'class':'hub__person__text_socials__container'})

                    name = name_class[0].div.h4.text.strip()

                    company_par = person.findAll('p', {'class':'hub__person__text__item'})

                    if len(company_par) == 0:

                        rank = None
                        company = None

                    elif len(company_par) == 1:

                        rank = company_par[0].text.strip()
                        company = None

                    else:

                        rank = company_par[0].text.strip()

                        company = company_par[1].text.strip().replace('@','')

                    facebook_class = person.findAll('a', {'class':'hub__person__social-list__link--facebook'})
                    if len(facebook_class) == 0:

                        facebook = None

                    else:

                        facebook = facebook_class[0]['href']

                    linkedin_class = person.findAll('a', {'class':'hub__person__social-list__link--linkedin'})
                    if len(linkedin_class)==0:

                        linkedin = None
                    else:

                        linkedin = linkedin_class[0]['href']

                    twitter_class = person.findAll('a', {'class':'hub__person__social-list__link--twitter'})
                    if len(twitter_class)==0:

                        twitter = None
                    else:

                        twitter = twitter_class[0]['href']


                    writer.writerow({'Name':name, 'Position':rank, 'Company':company, 'Twitter':twitter, 'LinkedIn':linkedin, 'Facebook':facebook})
                except:

                    pass

    except:

        pass

    finally:

        page += 1
