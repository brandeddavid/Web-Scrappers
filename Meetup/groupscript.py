from urllib.request import urlopen
import csv, json

offset = 0

while offset < 22:

    print('Scrapping offset:', offset)

    url = 'https://api.meetup.com/2/groups?&sign=true&photo-host=public&topic=cryptocurrency&page=200&offset=' + str(offset) + '&key=2317179606b581356403e49598658'

    links = []
    #page = urlopen(url).read().decode('utf-8')
    with urlopen(url) as url:

        data = json.loads(url.read().decode())

        with open ('cryptogroups.csv', 'a') as file:

            headers = ['Name', 'Members', 'Link', 'Country', 'State']

            writer = csv.DictWriter(file, fieldnames=headers)

            for group in data['results']:

                try:

                    name = group['name']
                    members = group['members']
                    link = group['link']
                    country = group['country']
                    state = group['state']

                except:

                    pass

                finally:

                    writer.writerow({'Name':name, 'Members':members, 'Link':link, 'Country':country, 'State':state})
                    name = ''
                    members = ''
                    link = ''
                    country = ''
                    state = ''

    offset += 1
