from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import csv



browser = webdriver.Firefox(executable_path=r'C:\Users\ict\Documents\My Docs\GIT Projects\Web-Scrappers\Global Energy Observatory\geckodriver.exe')
url = 'http://globalenergyobservatory.org/select.php?tgl=Edit'

countries = []

browser.get(url)

catergory = browser.find_element_by_xpath('//*[@id="db"]/option[1]')
catergory.click()
time.sleep(3)

ptype = browser.find_element_by_xpath('//*[@id="Type"]/option[1]')
ptype.click()
time.sleep(3)

country = browser.find_element_by_xpath('//*[@id="Country"]')
time.sleep(3)

for entry in country.text.split('\n'):

    countries.append(entry)

print(len(countries))
# country.click()

browser.close()