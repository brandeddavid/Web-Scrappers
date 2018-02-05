from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import csv

name = ''
status = ''
latitude = ''
longitude = ''
design_capacity = ''
plant_type = ''
plant_use = ''
location = ''
power_grid = ''
cooling_water = ''
year_comissioned = ''
owner = ''
per_owner = ''
ownership_type = ''
epc_contractor = ''
operating_company = ''
regulatory_authority = ''
financed_by = ''
reference = ''


count = 1

while count < 16:

    print (count)

    try:


        browser = webdriver.Firefox(executable_path=r'C:\Users\ict\Documents\My Docs\GIT Projects\Web-Scrappers\Global Energy Observatory\geckodriver.exe')

        url = 'http://globalenergyobservatory.org/select.php?tgl=Edit'

        browser.get(url)
        #time.sleep(2)

        catergory = browser.find_element_by_xpath('//*[@id="db"]/option[1]')
        catergory.click()
        time.sleep(3)

        type = browser.find_element_by_xpath('//*[@id="Type"]/option[7]')
        type.click()
        time.sleep(3)

        country = browser.find_element_by_xpath('//*[@id="Country"]/option[7]')
        country_name = country.text
        country.click()
        time.sleep(3)



        with open('SolarPV.csv', 'a', newline='') as file:

            headers = ['Name', 'Country', 'Status', 'Latitude', 'Longitude', 'Design Capacity', 'Location', 'Land Type', 'Mounting System', 'Power Grid', 'Owner', 'Per Owner', 'Ownership Type', 'EPC Contractor', 'Operating Company', 'Regulatory Authority', 'Financed By', 'Reference']

            writer = csv.DictWriter(file, fieldnames=headers)
            #writer.writeheader()

            state = browser.find_element_by_xpath('//*[@id="State"]/option[1]')
            state.click()
            time.sleep(3)

            plant = browser.find_element_by_xpath('//*[@id="Name"]/option[' + str(count) + ']')
            plant.click()
            time.sleep(3)

            button = browser.find_element_by_xpath('//*[@id="View and Edit Data"]')
            button.click()
            time.sleep(10)

            try:
                name = browser.find_element_by_xpath('//*[@id="Name"]').get_attribute('value')
                #print(name)

                status_dropdown = browser.find_element_by_xpath('//*[@id="Status_of_Plant_enumfield_itf"]')
                status = Select(status_dropdown).first_selected_option.text
                #print(status)

                latitude = browser.find_element_by_xpath('//*[@id="Latitude_Start"]').get_attribute('value')
                #print(latitude)

                longitude = browser.find_element_by_xpath('//*[@id="Longitude_Start"]').get_attribute('value')
                #print(longitude)

                design_capacity = browser.find_element_by_xpath('//*[@id="Design_Capacity_(MWe_Peak)_nbr"]').get_attribute('value')
                #print(design_capacity)


                location = browser.find_element_by_xpath('//*[@id="Location"]').get_attribute('value')
                #print(location)

                land_type_dropdown = browser.find_element_by_xpath('//*[@id="Type_of_Land_enumfield_rng1"]')
                land_type = Select(land_type_dropdown).first_selected_option.text
                #print(land_type)


                mounting_system_dropdown = browser.find_element_by_xpath('//*[@id="Mounting_System_enumfield_rng1"]')
                mounting_system = Select(mounting_system_dropdown).first_selected_option.text
                #print(mounting_system)

                power_grid_dropdown = browser.find_element_by_xpath('//*[@id="Electric_Power_Grid_Connected_To_enumfield_rng1"]')
                power_grid = Select(power_grid_dropdown).first_selected_option.text
                #print(power_grid)

                owner = browser.find_element_by_xpath('//*[@id="Owners1"]').get_attribute('value')
                #print(owner)

                per_owner = browser.find_element_by_xpath('//*[@id="%_Share_nbr1"]').get_attribute('value')
                #print(per_owner)

                ownership_type = browser.find_element_by_xpath('//*[@id="Type_of_Ownership"]').get_attribute('value')
                #print(ownership_type)

                epc_contractor = browser.find_element_by_xpath('//*[@id="Construction/EPC_Contractor"]').get_attribute('value')
                #print(epc_contractor)

                operating_company = browser.find_element_by_xpath('//*[@id="Operating_Company"]').get_attribute('value')
                #print(operating_company)

                regulatory_authority = browser.find_element_by_xpath('//*[@id="Regulatory_Authority"]').get_attribute('value')
                #print(regulatory_authority)

                financed_by = browser.find_element_by_xpath('//*[@id="Project_Financed_By"]').get_attribute('value')
                #print(financed_by)

                reference = browser.find_element_by_xpath('//*[@id="References1"]').get_attribute('value')
                #print(reference)

            except:

                pass

            finally:

                writer.writerow({'Name':name, 'Status':status, 'Country':country_name, 'Latitude':latitude, 'Longitude':longitude, 'Design Capacity':design_capacity, 'Location':location, 'Land Type':land_type, 'Mounting System':mounting_system, 'Power Grid':power_grid, 'Owner':owner, 'Per Owner':per_owner, 'Ownership Type':ownership_type, 'EPC Contractor':epc_contractor, 'Operating Company':operating_company, 'Regulatory Authority':regulatory_authority, 'Financed By':financed_by, 'Reference':reference})


    except:

        pass

    finally:

        browser.close()
        count += 1