from github import Github
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import json
import requests

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

def getLanguage(repoURL):
    languages = []
    response = requests.get(repoURL)
    response = json.loads(response.text) 
    for repo in response:
        if not repo['language']:
            pass
        else:
            languages.append(repo['language'])
    languages = set(languages)
    print(languages)

def getUsername():
    username_list = []
    page = 1
    while page < 11:
        try:
            print('Scrapping page', page)
            url = 'https://github.com/search?o=desc&p='+str(page)+'&q=location%3AChina+followers%3A%3C221&s=followers&type=Users'
            page_html = urlopen(url).read()
            soup = BeautifulSoup(page_html, 'html.parser')
            user_info_divs = soup.findAll("div", {"class":"user-list-info"})
            for user_info in user_info_divs:
                username_list.append(user_info.a.text)
            time.sleep(10)
        except Exception as e:
            print(e)
        finally:
            page += 1
    print(username_list)


if __name__ == '__main__':
    # getUsername()
    getLanguage('https://api.github.com/users/dorsywang/repos')

# g = Github("brandeddavid","marigi@98")
# repoLink = g.get_user('JustinFincher').repos_url
# getLanguage(repoURL=repoLink)
# user = g.get_user('JustinFincher')
# repos = user.get_repos().get_page(0)