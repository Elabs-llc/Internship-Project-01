# from scraper import scrape_election_news

# # Example URL to scrape
# url = 'https://www.ghanaweb.com/elections/2024/news'

# # Loop through the scraped data
# for data in scrape_election_news(url):
#     print(data)

import os
import webbrowser
from scraper import scrape_election_news  # Assuming the existing scraper logic is in scraper.py

def generate_html(news_data, output_file='scraped_news.html'):
    """
    Generate an HTML file to display the scraped news data.

    Args:
        news_data (list of dict): A list of dictionaries containing 'url' and 'title' of the news.
        output_file (str): The name of the output HTML file.
    """
    # Start creating HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scraped Election News</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #333; }
            ul { list-style-type: none; padding: 0; }
            li { margin: 10px 0; }
            a { text-decoration: none; color: #1a73e8; }
            a:hover { text-decoration: underline; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>Election News</h1>
        <ul>
    """

    # Add the news data to the HTML content
    for news in news_data:
        if 'error' in news:
            html_content += f"<li class='error'>Error: {news['error']}</li>"
        else:
            html_content += f"<li><a href='{news['url']}' target='_blank'>{news['title']}</a></li>"

    # Closing HTML tags
    html_content += """
        </ul>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"HTML file '{output_file}' generated successfully.")

    # Automatically open the file in the default web browser
    webbrowser.open('file://' + os.path.realpath(output_file))


def main():
    # Example URL to scrape
    url = 'https://www.ghanaweb.com/elections/2024/news'

    # Scrape the news data
    scraped_data = list(scrape_election_news(url))

    # Generate and open the HTML page
    generate_html(scraped_data)


if __name__ == "__main__":
    main()
