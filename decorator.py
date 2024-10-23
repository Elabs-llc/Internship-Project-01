import requests
from bs4 import BeautifulSoup


def scrape_web(url):
    response = requests.get(url)
    beauty_data = BeautifulSoup(response.text, 'html.parser')
    for item in beauty_data.find_all('div', class_= "feed-shared-update-v2__control-menu-container"):
        a_tag = item.find('a', class_='app-aware-link')
        yield {
            'feed_no': item.find('h2', class_='visually-hidden').text,
            'author': item.find('a', class_=''),
            'aria_label' : a_tag.get('aria-label') 
        }

url = 'https://www.linkedin.com/feed/'

for data in scrape_web(url):
    print(data)
