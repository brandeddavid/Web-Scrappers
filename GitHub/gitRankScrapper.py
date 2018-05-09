"""
[
    This file scrapes top 1000 GitHub profiles usernames from githubrank.com
    Using the username, it generates a file with profile information for those
    profile scrapped from GitHub
]

Returns:
    [file] -- [.csv file with top 1000 Chinese GitHub profiles with profile information]
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
from github import Github
import csv 

def login(username, password):
    """
    [Auth Function]

    Arguments:
        username {[str]} -- [GitHub username]
        password {[str]} -- [GitHub password]
    
    Returns:
        [object] -- [Authenticated GitHub object]
    """

    githubInstance = Github(username, password)
    return githubInstance

def scrapper(url, github_username, github_password):
    """
    [
        Scrapes GitHub users' profile information
    ]
    
    Arguments:
        url {[str]} -- [GitRank url]
        github_username {[str]} -- [GitHub username]
        github_password {[str]} -- [GitHub password]
    """

    username = ''
    github_name = ''
    github_bio = ''
    github_location = ''
    github_email = ''
    github_site = ''
    github_followers =  ''
    github_repo = ''
    github_languages = ''
    github_link = ''
    github = login(github_username, github_password)
    page_html = urlopen(url).read()
    soup = BeautifulSoup(page_html, 'html.parser')
    table = soup.find_all('table')
    trs = table[0].findAll('tr')
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
            except:
                pass
            finally:
                writer.writerow({'Name': github_name, 'Bio': github_bio, 'Location':github_location, 'Email': github_email, 'Site': github_site, 'Followers': github_followers, 'Repos': github_repo, 'Languages': github_languages, 'Link': github_link})
                username = ''
                github_name = ''
                github_bio = ''
                github_location = ''
                github_email = ''
                github_site = ''
                github_followers =  ''
                github_repo = ''
                github_languages = ''
                github_link = ''



if __name__ == '__main__':
    username = input('Enter your GitHub username: ')
    password = input('Enter your GitHub password: ')
    link = 'http://www.githubrank.com/'
    scrapper(link, username, password)