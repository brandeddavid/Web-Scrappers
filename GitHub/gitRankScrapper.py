"""[summary]

Returns:
    [type] -- [description]
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
from github import Github
import csv 

def login(username, password):
    """[summary]
    
    Arguments:
        username {[type]} -- [description]
        password {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """

    githubInstance = Github(username, password)
    return githubInstance

def scrapper(url):
    """[summary]
    
    Arguments:
        url {[type]} -- [description]
    """

    github = login('brandeddavid', 'marigi@98')
    page_html = urlopen(url).read()
    soup = BeautifulSoup(page_html, 'html.parser')
    table = soup.find_all('table')
    trs = table[0].findAll('tr')
    print (trs[0])
    with open('ChinaTop1000.csv', 'a', newline='') as outfile:
        headers = ['Name', 'Bio', 'Location', 'Email', 'Site', 'Followers', 'Repos', 'Languages', 'Link']
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()
        for tr in trs:
            try:
                tds = tr.findAll('td')
                print ('Getting info for top coder number', tds[0].text)
                username = tds[2].text
                user = github.get_user(username)
                github_name = user.name
                github_bio = user.bio
                github_location = user.location
                github_email = user.email
                github_site = user.blog
                github_followers = user.followers
                github_repo = user.repos_url
                github_languages = tds[5].text
                github_link = user.html_url
                writer.writerow({'Name': github_name, 'Bio': github_bio, 'Location':github_location, 'Email': github_email, 'Site': github_site, 'Followers': github_followers, 'Repo': github_repo, 'Languages': github_languages, 'Link': github_link})
            except:
                pass
            finally:
                username = None
                github_name = None
                github_bio = None
                github_email = None
                github_site = None
                github_followers =  None
                github_repo = None
                github_languages = None
                github_link = None



if __name__ == '__main__':
    link = 'http://www.githubrank.com/'
    scrapper(link)