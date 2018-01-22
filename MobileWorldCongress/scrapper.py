from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

page = 1

while page < 13:

    print('Scrapping page: ',  page)

    try:
        url = 'https://www.mobileworldcongress.com/conference-programmes/speakers/page/' + str(page) + '/'

        url_html = urlopen(url).read()
        soup = BeautifulSoup(url_html, 'html.parser')
        speaker_div = soup.findAll("div", {"class":"mod-in"})

        with open ("speakers.csv", "a", newline='') as file:

            headers = ['First Name', 'Second Name', 'Company', 'Position', 'Description', 'Tags']
            writer = csv.DictWriter(file, fieldnames=headers)

            for speaker in speaker_div:

                try:

                    name = speaker.h2.text

                    details = speaker.findAll('p')

                    company = details[0].text
                    position = details[1].text

                    inner = name.lower().replace(".","").replace(" ", "-")

                    try:

                        url2 = 'https://www.mobileworldcongress.com/speaker/' + inner + '/'

                        print("Inner url: ", url2)

                        url2_html = urlopen(url2).read()
                        soup2 = BeautifulSoup(url2_html, 'html.parser')
                        description_div = soup2.findAll("div", {"class":"api-description"})

                        if len(description_div) == 0:

                            description = None

                        else:

                            description = description_div[0].text.strip()

                        tag_div = soup2.findAll("div", {"class":"entity-tags"})

                        if len(tag_div) == 0:

                            tag = None

                        else:

                            tag = tag_div[0].text.strip()


                    except:

                        description = None
                        tag = None

                    finally:

                        description_div = []
                        tag_div = []

                    name = name.replace("Dr. ", "").split()

                    if len(name) == 2:

                        fname = name[0]
                        lname = name[1]

                    elif len(name) == 3:

                        fname = name[0]
                        lname = name[2]

                    writer.writerow({"First Name":fname, "Second Name":lname, "Company":company, "Position":position, "Description":description, "Tags":tag})
                except:

                    pass

    except:

        pass

    finally:

        page+=1
