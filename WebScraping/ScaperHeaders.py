#Librería de pareado de HTML XML
from bs4 import BeautifulSoup
import requests

url = "http://www.example.com"
page = requests.get(url)
#creamos un objeto de tipo beautifulsoup en el parser (html-parser o lxml)
soup = BeautifulSoup(page.content, "html.parser")
print(soup)
