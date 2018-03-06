from linkedin_scraper import Person
from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path=r'geckodriver.exe')

url = 'https://www.linkedin.com/uas/login?trk=hb_signin'

browser.get(url)

email = browser.find_element_by_xpath('//*[@id="session_key-login"]')
email.send_keys('david.mathenge98@gmail.com')
time.sleep(2)

password = browser.find_element_by_xpath('//*[@id="session_password-login"]')
password.send_keys('marigi@98')
time.sleep(2)

button = browser.find_element_by_xpath('//*[@id="btn-primary"]')
button.click()
time.sleep(5)

person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver = browser, scrape=False)

person.scrape(close_on_complete=False)

browser.close()



# browser.get('https://www.linkedin.com/search/results/people/?facetNetwork=%5B%22F%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH')
#
# connections = browser.find_element_by_xpath('//*[@id="ember5061"]/span[1]/span')
# time.sleep(10)
#
# print(connections)
#
# browser.close()
# person = Person('https://www.linkedin.com/in/brandeddavid/', driver=browser, scrape=True)
# time.sleep(10)
#
# print(person.scrape())