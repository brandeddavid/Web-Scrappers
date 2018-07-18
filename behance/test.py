import requests

url = "https://api.behance.net/v2/users?field=icon design&page=10&client_id=q3G4bMiRJPJhdsxcvcJZsWotTozGbFeU"
response = requests.get(url)
print(response)
print(len(response.json()['users']))
