import requests, re, csv, os, sys
from urllib import request
from bs4 import BeautifulSoup

urlList = []
#generic = ['admin', 'frontdesk', 'hiring', 'enroll', 'careers', 'career', 'info', 'online', 'help', 'desk', 'career', 'job', 'inquire', 'contact', 'post', 'master', 'general', 'admission', 'admissions', 'advise', 'advice', 'service', 'budget', 'department', 'board', 'noreply', 'webmaster', 'nr']

with open('url.csv', 'r') as k:

    reader = csv.reader(k, delimiter = ',')

    for item in reader:

        urlList.append(item[1])

with open('emails.csv', 'a', newline = '') as l:

    fieldnames = ['EMAILS', 'SITE STATUS']

    writer = csv.DictWriter(l, fieldnames=fieldnames)

    writer.writeheader()

    for url in urlList:

        print ('Url '+ str(urlList.index(url)+1) + ' of ' + str(len(urlList)))

        try:

            r = requests.get(url)

            emails = re.findall(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}', r.text)

            finalemails = []

            for email in set(emails):

                finalemails.append(email)

            for email in finalemails:

                if len(email) < 8:

                    finalemails.remove(email)

                elif email[0:email.index('@')] in generic:

                    finalemails.remove(email)

                else:

                    pass

        except:

            pass

        finally:

            writer.writerow({'EMAILS':[email for email in finalemails], 'SITE STATUS':r.status_code})

            emails = []
