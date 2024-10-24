import requests
from bs4 import BeautifulSoup
from errorhandler import retry_on_failure  # Import the retry decorator

@retry_on_failure(retries=3, delay=3)
def fetch_page(url):
    """
    Fetch the page content with retries in case of network errors.
    
    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        bytes: The content of the fetched page.
    """
    # Headers to simulate a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Will raise an HTTPError for bad responses
    return response.content

def scrape_election_news(url):
    """
    Scrapes election news from the given URL with error handling.

    Args:
        url (str): The URL of the webpage to scrape.

    Yields:
        dict: A dictionary with the election news data.
    """
    try:
        page_content = fetch_page(url)
        if page_content is None:
            yield {'error': 'Failed to retrieve the webpage after multiple attempts.'}
            return

        beauty_data = BeautifulSoup(page_content, 'html.parser')

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

    except Exception as e:
        yield {'error': f"An unexpected error occurred: {str(e)}"}
