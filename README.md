
# Sorting and Filtering Election News with Lambda Functions

## Description
This part of the project enhances data processing capabilities by using lambda functions to efficiently sort and filter election news data scraped from GhanaWeb's Election page. It enables targeted extraction based on specific dates and keywords, supporting a streamlined data analysis and reporting process.

## Features
- **Sort by Date:** Uses lambda functions to sort election news articles in descending order by publication date.
- **Keyword-Based Filtering:** Allows keyword filtering within article titles to capture relevant election news topics.
- **Efficient and Readable:** The lambda functions provide concise, on-the-fly sorting and filtering, improving code readability and reducing complexity.
- **Error Handling:** If a date or keyword is missing, appropriate fallbacks and error messages are included to maintain process continuity.

## How the Sorting and Filtering Work
### Sort by Date:
- Sorts articles in descending order based on the publication date.
- Uses Python's `datetime` module and lambda expressions to handle varying date formats and provide a default minimum date if none is available.

### Keyword Filtering:
- Filters articles based on a list of keywords.
- Employs a lambda function to check for keyword matches in the title, enhancing content relevance.
