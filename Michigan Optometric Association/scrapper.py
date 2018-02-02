from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import csv

browser = webdriver.Firefox()

url = 'https://www.themoa.org/aws/MOA/pt/sp/doctor_locator'

with open('292-301.csv', 'r') as infile:

    reader = csv.reader(infile, delimiter=',')

    for row in reader:

        browser.get(url)

        lname = browser.find_element_by_xpath('//*[@id="SRCH_field__0"]')
        lname.send_keys(row[2])

        pname = browser.find_element_by_xpath('//*[@id="SRCH_field__1"]')
        pname.clear()

        speciality = browser.find_element_by_xpath('//*[@id="content"]/div[2]/form/dl/dd[3]/select/option[contains(text(), "Any")]').click()

        address = browser.find_element_by_xpath('//*[@id="SRCH_field__3"]')
        address.clear()

        distance = browser.find_element_by_xpath('//*[@id="content"]/div[2]/form/dl/dd[5]/select/option[contains(text(), "Any")]').click()

        button = browser.find_element_by_xpath('//*[@id="content"]/div[2]/form/dl/dd[6]/input')
        button.click()

        time.sleep(3)

        with open('contactinfo.csv', 'a', newline='') as outfile:

            headers = ['Name', 'Contact']
            writer = csv.DictWriter(outfile, fieldnames=headers)

            listings = browser.find_elements_by_class_name('directory_listing')

            for listing in listings:

                print(listing.text)

            browser.close()