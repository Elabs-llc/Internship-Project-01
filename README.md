# Web Scraping and Data Processing Tool 

## Description
This Python-based tool scrapes data from multiple websites, processes the data, and generates reports. It incorporates the use of decorators, generators, lambda expressions, and list comprehensions to optimize functionality and performance.

## Features
- **Decorators:**
  - Logs the execution time of web scraping functions.
  - Retries failed web requests with a custom retry and delay mechanism.
- **Generators:**
  - Yields scraped data in real-time, reducing memory overhead.
- **Lambda Expressions:**
  - Used for sorting and filtering scraped data efficiently.
- **List Comprehension:**
  - Cleans and normalizes scraped data.

## How to Use
1. Clone this repository.
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python scraper.py
   ```

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Contributors
This project was developed with contributions from the following team members:

- **[Edwin Asare]** - Project Lead, Data Processing & Generators
- **[Blessing Laryea]** - Data Cleaning & List Comprehensions
- **[Victor Kwame Mawuli]** - Web Scraping & Error Handling
- **[Kwadwo Tuffour Quayson]** - Sorting, Filtering & Lambda Functions

## Task Allocation for Contributors

1. **Web Scraping & Error Handling**:
   - **Victor Kwame Mawuli**: Responsible for implementing web scraping logic using `requests` and `BeautifulSoup`, and applying the retry decorator for error handling and failed web requests.

2. **Data Processing & Generators**:
   - **Edwin Asare**: Focuses on processing the scraped data in real-time using Python generators to yield results without overloading memory.

3. **Sorting, Filtering & Lambda Functions**:
   - **Kwadwo Tuffour Quayson**: Implements sorting and filtering functionality using lambda expressions to manage the scraped data (e.g., sorting by price, filtering by criteria).

4. **Data Cleaning & List Comprehensions**:
   - **Blessing Laryea**: Uses list comprehensions to clean, transform, and normalize the scraped data, such as removing HTML tags and formatting text fields.

## License
This project is licensed under the MIT License.
