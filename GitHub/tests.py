from github import Github
import requests
import json

# url = 'https://api.github.com/search/users?q=location%3AChina&s=followers:10000&page=1&per_page=100'
# response = requests.get(url)
# content = json.loads(response.text)
# print(len(content['items']))

github = Github('brandeddavid', 'marigi@98')
repos = github.get_user('edokeh').get_repos()
for repo in repos:
    print(repo.language)