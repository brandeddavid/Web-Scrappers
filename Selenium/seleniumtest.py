from selenium import webdriver
import time

browser = webdriver.Firefox()

url = 'http://www.lexisnexis.com/hottopics/lnacademic/'

browser.get(url)
time.sleep(2)

browser.find_element_by_id('terms').clear()
browser.find_element_by_id('terms').send_keys('balloon')