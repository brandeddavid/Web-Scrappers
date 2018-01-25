from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

browser = webdriver.Firefox()

url = 'http://www.dld-conference.com/speakers'

browser.get(url)
#time.sleep(2)

fname = browser.find_element_by_id('speaker-first-name-search')
fname.clear()
#fname.send_keys('Mark')
#time.sleep(2)

lname = browser.find_element_by_id('speaker-last-name-search')
lname.clear()
#lname.send_keys('Zuckerberg')
#time.sleep(2)

browser.find_element_by_id('company').clear()
browser.find_element_by_xpath('//*[@id="conference"]/option[contains(text(), "Conference")]').click()
browser.find_element_by_xpath('//*[@id="category"]/option[contains(text(), "Field of Operation")]').click()

time.sleep(1200)

#element = browser.find_element_by_class_name('speakers-page')
#actions = ActionChains(browser)
#actions.move_to_element(element).perform()
#time.sleep(20)
#element.location_once_scrolled_into_view
#time.sleep(20)

links = []

content = browser.find_elements_by_class_name('speaker-item')

for item in content:

    inner_content = item.find_element_by_class_name('speaker-container')

    link = inner_content.get_attribute('href')

    links.append(link)

browser.close()
#print(links)
print(len(links))

with open('links20.csv', 'a', newline='') as file:

    headers = ['URLS']
    writer = csv.DictWriter(file, fieldnames=headers)
    #writer.writeheader()

    for url in links:

        writer.writerow({'URLS':url})
