import requests
from bs4 import BeautifulSoup


def scrape_web(url):
    """
    Scrapes election news from a given URL, specifically from a webpage with a list of election-related news - Ghana Web.

    Args:
        url (str): The URL of the webpage to scrape.

    Yields:
        dict: A dictionary containing:
            - 'url': The full URL to the news article.
            - 'title': The title of the news article.
            - 'error' (optional): If no news items are found or the list cannot be scraped.

    """

    # Headers to simulate a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        beauty_data = BeautifulSoup(response.content, 'html.parser')

        # Find the election news list by the specified class
        election_news = beauty_data.find('ul', class_="election_list")
        
        if election_news:
            
            # Find all list items within the election news section
            news_items = election_news.find_all('li')

            if not news_items:
                yield {'error': 'No news items found on the page'}

            # Extract URL and title from each news item
            for news in news_items:

                url = news.find('a')

                if url and url.get('href'):

                    relative_url = url.get('href')

                    base_url = 'https://www.ghanaweb.com'

                    # Construct the full URL if the href is relative
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

# Example URL to scrape
url = 'https://www.ghanaweb.com/elections/2024/news'

# Loop through  the scraped data

for data in scrape_web(url):
    print(data)
