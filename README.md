# Election News Web Scraper

A Python-based web scraping tool that scrapes election-related news from multiple websites, processes the data, and displays it on a dynamically generated web page. The tool incorporates error handling using decorators, along with the use of `BeautifulSoup` for parsing HTML content.

## Features

- Web Scraping: Scrapes news articles from a target election news website using `requests` and `BeautifulSoup`.
- Error Handling: Includes error handling via a custom `retry_on_failure` decorator for robust web requests.
- Dynamic HTML Generation: Generates an HTML page from the scraped data and opens it in a web browser.
- Memory Optimization: Uses Python generators to yield scraped data, reducing memory overhead.

## Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package manager)

### Dependencies

- `requests`: For making HTTP requests to the target website.
- `beautifulsoup4`: For parsing HTML content.
- `webbrowser`: For opening the generated HTML in a web browser.

## Usage

1. Run the Web Scraper:

   ```bash
   python main.py
   ```

   This command will:
   - Scrape election news from the target URL.
   - Generate an HTML file called `scraped_news.html`.
   - Automatically open the generated HTML file in your default web browser.

2. Accessing the HTML Output:
   - The generated HTML file is (`scraped_news.html`) in the project's root directory.
   - The file will contain a list of news articles with clickable links.

## Code Walkthrough

### scraper.py

Contains the primary web scraping logic:

- Uses `BeautifulSoup` to parse HTML from a target URL.
- Extracts news articles by locating specific HTML elements.
- Yields each news item as a dictionary containing the `title` and `url`.

### errorhandler.py

Contains the `retry_on_failure` decorator:

- Handles network-related errors (e.g., connection timeouts, HTTP errors).
- Retries failed web requests a specified number of times with a delay between attempts.

### html_generator.py

Contains the `generate_html` generator:

- Generates an HTML file with the collected data.
- Opens the generated HTML file automatically in the default web browser.

### sorting_and_filter.py

Contains the `sort_election_news_by_date`, `filter_election_news_by_keywords`, `process_election_news` and `print_election_news` function:

- **Sort by Date:** Uses lambda functions to sort election news articles in descending order by publication date.
- **Keyword-Based Filtering:** Allows keyword filtering within article titles to capture relevant election news topics.
- **Efficient and Readable:** The lambda functions provide concise, on-the-fly sorting and filtering, improving code readability and reducing complexity.
- **Error Handling:** If a date or keyword is missing, appropriate fallbacks and error messages are included to maintain process continuity.

### data_cleaning_list_comprehension.py

Contains data cleaning functions utilizing list comprehensions:

- **Data Processing:** Cleans and processes raw scraped data by removing unwanted characters or formatting issues.
- **Efficient Data Transformation:** Uses list comprehensions for efficient iteration and transformation of data items.
- **Prepared Data for Further Use:** Ensures the cleaned data is ready for further processing or display, reducing manual data handling efforts.

### logs.py

Contains logging configurations and utility functions:

- **Logging Configuration:** Sets up the logging configuration to capture INFO level logs and above in logs.log.
- **Function Execution Logging:** Includes decorators to log function execution times and return values, enhancing the visibility of data flow within the application.

### main.py

Main script for running the scraping process:

- Uses the scraper to collect news data.

## Customization

### Change Target URL

To scrape data from a different URL, modify the `url` variable in `scraper.py`:

```python
# Modify this line in scraper.py
url = 'https://www.ghanaweb.com/elections/2024/news'
```
