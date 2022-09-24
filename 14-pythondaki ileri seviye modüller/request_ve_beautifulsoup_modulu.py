import requests
from bs4 import BeautifulSoup

url = "https://www.natgeotv.com/tr"
response = requests.get(url)

print(response) # bilgileri çekip çekmediğimize bakabiliriz.

html_iceriği = response.content

soup = BeautifulSoup(html_iceriği,"html.parser")

for i in soup.find_all("a"):
    print(i.get("href"))
    print("**********************")