import requests, json, csv

# url = "https://api.behance.net/v2/users?field=design&page=23&client_id=q3G4bMiRJPJhdsxcvcJZsWotTozGbFeU"

def scrapper(field, max_page, key):
    page = 1
    with open(field.title()+'.csv', 'a', newline='') as file:
        fieldnames = ["First", "Last", "Username", "City", "State", "Country", "Company", "Occupation", "Fields"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        while page < int(max_page)+1:
            try:
                url = "https://api.behance.net/v2/users?field="+field+"&page="+str(page)+"&client_id="+key
                response = requests.get(url)
                for user in response.json()['users']:
                    print("Page", page, "User", response.json()['users'].index(user)+1, "of", len(response.json()['users']))
                    try:
                        f_name = user['first_name']
                        l_name = user['last_name']
                        username = user['username']
                        city = user['city']
                        state = user['state']
                        country = user['country']
                        company = user['company']
                        occupation = user['occupation']
                        fields = str(user['fields'])
                    except Exception as e:
                        print(e)
                    finally:
                        writer.writerow({"First": f_name, "Last": l_name, "Username": username, "City": city, "State": state, "Country": country, "Company": company, "Occupation": occupation, "Fields": fields.replace("[", "").replace("]", "")})
                        f_name = ""
                        l_name = ""
                        username = ""
                        city = ""
                        state = ""
                        country = ""
                        company = ""
                        occupation = ""
                        fields = ""
            except Exception as e:
                print(e)
            finally:
                page+=1


if __name__ == '__main__':
    field = input("Enter field to search: ")
    max_page = input("Enter No. of pages: ")
    key = input("Enter client ID: ")
    scrapper(field, max_page, key)
