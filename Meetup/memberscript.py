from urllib.request import urlopen
import csv, json, math


group = '4-Women-Entrepreneurs'

urlj = 'https://api.meetup.com/2/members?&sign=true&photo-host=public&group_urlname=' + group + '&page=20&key=2317179606b581356403e49598658'
with urlopen(urlj) as urlj:

    jsn = json.loads(urlj.read().decode())

    total_count = jsn['meta']['total_count']

    count = math.ceil(total_count/200)

offset = 0

while offset < count:

    print('Offset:', offset)

    url = 'https://api.meetup.com/2/members?&sign=true&photo-host=public&group_urlname=' + group + '&page=200&offset=' + str(offset) + '&key=2317179606b581356403e49598658'

    with urlopen(url) as url:

        data = json.loads(url.read().decode())

        with open('members.csv', 'a', newline='') as file:

            headers = ['Name', 'Country', 'City', 'Link', 'Group', 'Status']
            writer = csv.DictWriter(file, fieldnames=headers)

            for person in data['results']:

                try:

                    name = person['name']
                    country = person['country']
                    city = person['city']
                    link = person['link']
                    status = person['status']

                except:

                    pass

                finally:

                    writer.writerow({'Name':name, 'Country':country, 'City':city, 'Link':link, 'Group':group, 'Status':status})
    offset += 1
