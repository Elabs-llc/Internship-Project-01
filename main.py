from html_generator import generate_html
from scraper import scrape_election_news


"""
main.py

This script scrapes election news from a specified URL and generates an HTML 
file to display the scraped data.

Dependencies:
- scraper: A module responsible for scraping election news from a given URL.
- html_generator: A module that provides functionality to generate HTML files 
  from the scraped news data.

Main Functions:
- main(): 
    Scrapes news articles from a predefined URL and generates an HTML page 
    containing the scraped data, which is then displayed in the web browser.

This script serves as the entry point for running the web scraping and 
HTML generation process.
"""
def main():
    # Example URL to scrape
    url = 'https://www.ghanaweb.com/elections/2024/news'

    # Scrape the news data
    scraped_data = list(scrape_election_news(url))

    # Generate and open the HTML page
    generate_html(scraped_data)


if __name__ == "__main__":
    main()
