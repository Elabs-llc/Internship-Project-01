from datetime import datetime

from logs import log_execution_time, log_message
from scraper import scrape_election_news

# Log message & execution time
@log_message(message='Election news sorted by date ')
@log_execution_time
def sort_election_news_by_date(scraped_data):
    """
    Sorts election news by publication date in descending order (latest first).

    Args:
        scraped_data (list of dict): The scraped election news data.

    Returns:
        list of dict: Sorted list of news items.
    """
    return sorted(
        scraped_data,
        key=lambda x: datetime.strptime(x['date'], '%B %d, %Y') if 'date' in x and x['date'] != 'No date available' else datetime.min,
        reverse=True
    )

# Log message & execution time
@log_message(message='Filtered election news successfully!')
@log_execution_time
def filter_election_news_by_keywords(sorted_data, filter_keywords):
    """
    Filters election news articles based on specific keywords in the title.

    Args:
        sorted_data (list of dict): The sorted election news data.
        filter_keywords (list of str): List of keywords to filter titles.

    Returns:
        list of dict: Filtered list of news items containing the keywords.
    """
    return list(
        filter(lambda x: any(kw.lower() in x.get('title', '').lower() for kw in filter_keywords), sorted_data)
    )

# Log message & execution time
@log_message(message='Election news processed successfully ! and took: ')
@log_execution_time
def process_election_news(url, filter_keywords):
    """
    Fetches, sorts, and filters election news articles.

    Args:
        url (str): The URL to scrape for election news.
        filter_keywords (list of str): List of keywords for filtering.

    Returns:
        list of dict: Processed news articles.
    """
    # Scrape the election news data
    scraped_data = list(scrape_election_news(url))  # Ensure scrape_election_news is defined or imported

    # Sort the data by date
    sorted_data = sort_election_news_by_date(scraped_data)

    # Filter the data by keywords
    filtered_data = filter_election_news_by_keywords(sorted_data, filter_keywords)

    return filtered_data

# Log message & execution time
@log_message(message='Printed processed election news articles.')
@log_execution_time
def print_election_news(processed_data):
    """Prints the processed election news articles."""
    for article in processed_data:
        print(f"Title: {article.get('title', 'No title available')}, Date: {article.get('date', 'No date available')}")
        print(f"URL: {article.get('url', 'No URL available')}\n")