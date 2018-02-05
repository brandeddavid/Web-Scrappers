from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import csv



browser = webdriver.Firefox(executable_path=r'C:\Users\ict\Documents\My Docs\GIT Projects\Web-Scrappers\Global Energy Observatory\geckodriver.exe')
url = 'http://globalenergyobservatory.org/select.php?tgl=Edit'

plants = []

browser.get(url)

catergory = browser.find_element_by_xpath('//*[@id="db"]/option[1]')
catergory.click()
time.sleep(3)

ptype = browser.find_element_by_xpath('//*[@id="Type"]/option[5]')
ptype.click()
time.sleep(3)

country = browser.find_element_by_xpath('//*[@id="Country"]/option[32]')
country.click()
time.sleep(3)

state = browser.find_element_by_xpath('//*[@id="State"]/option[1]')
state.click()
time.sleep(3)

plant = browser.find_element_by_xpath('//*[@id="Name"]')
time.sleep(3)


for entry in plant.text.split('\n'):

    plants.append(entry)

print(len(plants))
# country.click()

browser.close()