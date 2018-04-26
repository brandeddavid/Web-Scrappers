from urllib.request import urlopen
import csv, json

def groups(category, key):
    offset = 0
    while offset < 22:
        print('Scrapping offset:', offset)
        url = 'https://api.meetup.com/2/groups?&sign=true&photo-host=public&topic='+category+'&page=200&offset=' + str(offset) + '&key=' + key 
        #2317179606b581356403e49598658
        #page = urlopen(url).read().decode('utf-8')
        with urlopen(url) as url:
            data = json.loads(url.read().decode())
            with open (category + '.csv', 'a', newline='') as file:
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


if __name__ == '__main__':

    print("Enter Search Category:")
    category = input(">")
    print("Enter Key:")
    key = input(">")
    groups(category,key)