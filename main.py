import requests
import pprint
from bs4 import BeautifulSoup

URL = 'https://realpython.com/beautiful-soup-web-scraper-python/#what-is-web-scraping'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='find-elements-by-html-class-name')

# print(results)
print(results.prettify())
