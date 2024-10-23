# Web Scraping: Election News from GhanaWeb

## Project Overview

This part of the project focuses on scraping election-related news from the [GhanaWeb Elections page](https://www.ghanaweb.com/elections/2024/news). The goal is to extract useful data such as the article titles and URLs of election news articles. This data can then be used for analysis or reporting purposes. 

## Features

- Scrapes election news titles and URLs from a specific `ul` tag with the class `election_list`.
- Handles both relative and absolute URLs for news articles.
- Yields structured data in the form of Python dictionaries, making it easy to consume in other parts of the project.
- Provides meaningful messages when there is no news content or when scraping fails.

## How the Scraping Works

1. **Send a Request**: A GET request is made to the GhanaWeb elections page using the Python `requests` library.
2. **Parse the Page**: The response is parsed using `BeautifulSoup` to extract relevant HTML elements.
3. **Extract Data**: The code looks for the `ul` element with the class `election_list` and then iterates through each `li` element (news item).
4. **Handle URLs**: It checks if the news article has a valid URL, constructs a full URL if necessary, and yields a dictionary with the `title` and `url` of each news item.
5. **Error Handling**: If the `ul` tag is not found or the list is empty, appropriate error messages are returned.

## Code

```python
import requests
from bs4 import BeautifulSoup

def scrape_web(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        beauty_data = BeautifulSoup(response.content, 'html.parser')

        election_news = beauty_data.find('ul', class_="election_list")
        
        if election_news:
            news_items = election_news.find_all('li')

            if not news_items:
                yield {'error': 'No news items found on the page'}

            for news in news_items:
                url = news.find('a')

                if url and url.get('href'):
                    relative_url = url.get('href')
                    base_url = 'https://www.ghanaweb.com'
                    full_url = base_url + relative_url if relative_url.startswith('/') else relative_url

                    yield {
                        'url': full_url,
                        'title': url.text.strip(),
                    }
                else:
                    yield {
                        'url': None,
                        'title': url.text.strip() if url else 'No title found!',
                    }
        else:
            yield {'error': 'Could not find the election list on the page'}

    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

url = 'https://www.ghanaweb.com/elections/2024/news'

for data in scrape_web(url):
    print(data)
