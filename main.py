from html_generator import generate_html
from scraper import scrape_election_news
from sorting_and_filter import process_election_news, print_election_news


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

    # Prompt the user to enter keywords for filtering, separated by commas
    '''
    Remove comments to enable user input for filter keywords. and comments the filter_keywords variable below
    '''
    # user_input = input("Enter keywords for filtering (separate by commas): ")
    # filter_keywords = [keyword.strip() for keyword in user_input.split(',') if keyword.strip()]

    # Set filter keywords (example: filter by 'election' or 'Ghana')
    filter_keywords = ['election', 'Ghana'] # comment this if you want to use user input

    # Scrape the news data
    #scraped_data = list(scrape_election_news(url))

    # Process news data by fetching, sorting, and filtering
    processed_data = process_election_news(url, filter_keywords)

    # Print the processed data to console (optional) | displays the
    # filtered and sorted news data in the console for verification.
    print_election_news(processed_data)

    # Generate and open the HTML page with the filtered and sorted data
    generate_html(processed_data)


if __name__ == "__main__":
    main()
