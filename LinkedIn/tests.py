from pylinkedin.utils import CustomRequest
from pylinkedin.scraper import LinkedinItem


url ='https://www.linkedin.com/in/andre-iguodala-65b48ab5'

c = CustomRequest() # default with rotating proxies
#c = CustomRequest(rotating_ua=True) # without rotating user-agent
c = CustomRequest(list_proxies=[{'https':'http://186.233.94.106:8080', 'http':'http://186.233.94.106:8080'}])

l = LinkedinItem(url=url)
l = LinkedinItem(html_string=profile_string)