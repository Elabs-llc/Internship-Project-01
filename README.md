# Election News Web Scraper

A Python-based web scraping tool that scrapes election-related news from multiple websites, processes the data, and displays it on a dynamically generated web page. The tool incorporates error handling using decorators, along with the use of `BeautifulSoup` for parsing HTML content.

# Features

- Web Scraping: Scrapes news articles from a target election news website using `requests` and `BeautifulSoup`.
- Error Handling: Includes error handling via a custom `retry_on_failure` decorator for robust web requests.
- Dynamic HTML Generation: Generates an HTML page from the scraped data and opens it in a web browser.
- Memory Optimization: Uses Python generators to yield scraped data, reducing memory overhead.

# Installation

## Prerequisites

- Python 3.7 or higher
- Pip (Python package manager)

## Dependencies

- `requests`: For making HTTP requests to the target website.
- `beautifulsoup4`: For parsing HTML content.
- `webbrowser`: For opening the generated HTML in a web browser.

# Usage

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

# Code Walkthrough

## scraper.py

Contains the primary web scraping logic:

- Uses `BeautifulSoup` to parse HTML from a target URL.
- Extracts news articles by locating specific HTML elements.
- Yields each news item as a dictionary containing the `title` and `url`.

## errorhandler.py

Contains the `retry_on_failure` decorator:

- Handles network-related errors (e.g., connection timeouts, HTTP errors).
- Retries failed web requests a specified number of times with a delay between attempts.

# main.py

Main script for running the scraping process:

- Uses the scraper to collect news data.
- Generates an HTML file with the collected data.
- Opens the generated HTML file automatically in the default web browser.

# Customization

# Change Target URL

To scrape data from a different URL, modify the `url` variable in `scrape_to_html.py`:

```python
# Modify this line in scrape_to_html.py
url = 'https://www.ghanaweb.com/elections/2024/news'
```
