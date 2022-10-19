import requests
from bs4 import BeautifulSoup

response = requests.get(
	url="https://www.dr.dk/nyheder"
)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find('div', class_="hydra-latest-news-page-short-news__heading").find('span', class_="dre-hyphenate-text")

print(title.text)