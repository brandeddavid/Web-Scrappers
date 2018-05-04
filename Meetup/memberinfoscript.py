from urllib.request import urlopen
import csv, json, math
import time

idList = []

def profIds(file):
    with open (file, 'r') as infile:
        reader = csv.reader(infile, delimiter=',')
        for row in reader:
            id = row[3].split('/')[-1]
            idList.append(id)
    return idList

def bio(id, key):
    try:
        url = 'https://api.meetup.com/2/member/'+id+'?&sign=true&photo-host=public&page=20&key='+key
        with urlopen(url) as url:
            data = json.loads(url.read().decode())
            biography = data['bio'].strip()
    except:
        biography = ''
        pass
    finally:
        return biography

def twitter(id, key):
    try:
        url = 'https://api.meetup.com/2/member/'+id+'?&sign=true&photo-host=public&page=20&key='+key
        with urlopen(url) as url:
            data = json.loads(url.read().decode())
            twitterLink = data['other_services']['twitter']['identifier'].strip()
    except:
        twitterLink = ''
        pass 
    finally:
        return twitterLink

def facebook(id, key):
    try:
        url = 'https://api.meetup.com/2/member/'+id+'?&sign=true&photo-host=public&page=20&key='+key
        with urlopen(url) as url:
            data = json.loads(url.read().decode())
            facebookLink = data['other_services']['facebook']['identifier'].strip()
    except:
        facebookLink = ''
        pass
    finally:
        return facebookLink


if __name__ == '__main__':
    membersFile = input('Please enter the file name\n>')
    ids = profIds(membersFile)
    time.sleep(20)
    key = '2317179606b581356403e49598658'
    with open('memberinfo.csv', 'a', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['ID', 'Bio', 'Facebook', 'Twitter'])
        for id in ids:
            print ("Searching", ids.index(id)+1, "of", len(ids))
            try:
                biog = bio(id, key)
                facebookL = facebook(id, key)
                twitterL = twitter(id, key)
            except:
                pass
            finally:
                writer.writerow({'ID':id, 'Bio':biog, 'Facebook':facebookL, 'Twitter': twitterL})
