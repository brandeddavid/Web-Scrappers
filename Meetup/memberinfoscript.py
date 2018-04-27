from urllib.request import urlopen
import csv, json, math
import time

def memberInfo(ids, key):
    with open('memberinfo.csv', 'a', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['ID', 'Bio', 'Facebook', 'Twitter'])
        for id in ids:
            url = 'https://api.meetup.com/2/member/'+id+'?&sign=true&photo-host=public&page=20&key='+key
            with urlopen(url) as url:
                bio = ''
                facebook = ''
                twitter = ''
                try:
                    data = json.loads(url.read().decode())
                    bio = data['bio'].strip()
                    twitter = data['other_services']['twitter']['identifier'].strip()
                    facebook = data['other_services']['facebook']['identifier'].strip()
                except:
                    pass
                finally:
                    writer.writerow({'ID':id, 'Bio':bio, 'Facebook':facebook, 'Twitter': twitter})
                    bio = ''
                    facebook = ''
                    twitter = ''


if __name__ == '__main__':
    profId = ['38661082', '183557497', '13501498']
    key = '2317179606b581356403e49598658'
    print(memberInfo(profId, key))
