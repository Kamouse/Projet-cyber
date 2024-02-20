import requests

url = "https://www.gov.uk"
page = requests.get(url)
print(page.content)
