from selenium import webdriver
import csv

page = 340
while page < 3950:
    browser = webdriver.Firefox()
    try:
        url = 'https://www.sideprojectors.com/project/home#search/all/all/all/all/all/all/all/all/all/all/10/' + str(page)
        browser.get(url)
        with open('projectsloop.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Title", "Platform", "Owner", "Description"])
            try:
                projects = browser.find_elements_by_class_name('project')
                for project in projects:
                    try:
                        project_title = project.find_element_by_class_name('project-title').text 
                        platform = project.find_element_by_class_name('display-table-cell').text
                        owner = project.find_element_by_class_name('color-grey').text
                        description = project.find_element_by_class_name('color-grey-d3').text
                    except Exception as e:
                        print(e)
                        pass
                    finally:
                        writer.writerow({"Title": project_title, "Platform": platform, "Owner": owner, "Description": description})
            except Exception as e:
                print(e)
                pass
    except Exception as e:
        print(e)
        pass
    finally:
        browser.close()
        page += 10
