from github import Github

g = Github("brandeddavid","marigi@98")
user = g.get_user('JustinFincher')
for repo in user.get_repos():
    print(repo.name)


# print(help(user))