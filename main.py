from data_cleaning_list_comprehension import ElectionDataCleaner
from html_generator import generate_html
from scraper import scrape_election_news
from sorting_and_filter import filter_election_news_by_keywords, process_election_news, print_election_news


"""
main.py

This script scrapes election news from a specified URL, cleans and processes the data,
and generates an HTML file to display the results.

Dependencies:
- scraper: A module responsible for scraping election news from a given URL.
- html_generator: A module that provides functionality to generate HTML files 
  from the cleaned and processed news data.
- sorting_and_filter: A module containing functions for processing news data
  (filtering and potentially sorting).

Main Functions:
- main():
  - Scrapes news articles from a predefined URL.
  - Cleans and processes the articles (including filtering by keywords if enabled).
  - Generates an HTML page containing the processed data.

This script serves as the entry point for running the web scraping, data processing,
and HTML generation process.
"""
def main():
    # check if keywords is enabled
    isKeywordsEnabled = False

    # Example URL to scrape
    url = 'https://www.ghanaweb.com/elections/2024/news'

    # Scrape raw news articles
    scraped_data = list(scrape_election_news(url))

    # Initialize the cleaner and clean articles
    cleaner = ElectionDataCleaner()
    cleaned_data  = cleaner.clean_articles(scraped_data)
    # print("Cleaned Data:")
    # print(cleaned_data)

    # Prompt the user to enter keywords for filtering, separated by commas
    '''
    Remove comments to enable user input for filter keywords. and comments the filter_keywords variable below
    '''
    # user_input = input("Enter keywords to search for (comma-separated): ")
    # keywords = [kw.strip() for kw in user_input.split(",") if kw.strip()]
    keywords = cleaner.election_keywords

    # Process news data by fetching, sorting, and filtering if enabled
    keyword_filtered_articles =  filter_election_news_by_keywords(cleaned_data, keywords) if isKeywordsEnabled else cleaned_data
    # print("Data for HTML:", keyword_filtered_articles)

    # Print the processed data to console (optional) | displays the
    # filtered and sorted news data in the console for verification.
    # print_election_news(cleaned_data )

    # Generate and open the HTML page with the filtered and sorted data
    generate_html(keyword_filtered_articles)


if __name__ == "__main__":
    main()
