from linkedin_scraper import Person
from selenium import webdriver
import time

browser = webdriver.Chrome()

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

person = Person('https://www.linkedin.com/in/brandeddavid/', driver=browser, scrape=True)
time.sleep(10)

print(person.scrape())