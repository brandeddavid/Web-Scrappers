from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

browser = webdriver.Firefox()

url = 'http://globalenergyobservatory.org/select.php?tgl=Edit'

browser.get(url)
#time.sleep(2)

catergory = browser.find_element_by_xpath('//*[@id="db"]/option[1]')
catergory.click()
time.sleep(3)

type = browser.find_element_by_xpath('//*[@id="Type"]/option[1]')
type.click()
time.sleep(3)

country = browser.find_element_by_xpath('//*[@id="Country"]/option[1]')
country.click()
time.sleep(3)

state = browser.find_element_by_xpath('//*[@id="State"]/option[1]')
state.click()
time.sleep(3)

plant = browser.find_element_by_xpath('//*[@id="Name"]/option')
plant.click()
time.sleep(3)

button = browser.find_element_by_xpath('//*[@id="View and Edit Data"]')
button.click()
time.sleep(10)

name = browser.find_element_by_xpath('//*[@id="Name"]').get_attribute('value')
print(name)

latitude = browser.find_element_by_xpath('//*[@id="Latitude_Start"]').get_attribute('value')
print(latitude)

longitude = browser.find_element_by_xpath('//*[@id="Longitude_Start"]').get_attribute('value')
print(longitude)

design_capacity = browser.find_element_by_xpath('//*[@id="Design_Capacity_(MWe)_nbr"]').get_attribute('value')
print(design_capacity)

location = browser.find_element_by_xpath('//*[@id="Location"]').get_attribute('value')
print(location)

owner = browser.find_element_by_xpath('//*[@id="Owners1"]').get_attribute('value')
print(owner)

reference1 = browser.find_element_by_xpath('//*[@id="References1"]').get_attribute('value')
print(reference1)

reference2 = browser.find_element_by_xpath('//*[@id="References2"]').get_attribute('value')
print(reference2)