import os
import webbrowser

"""
html_generator.py

This module contains functions for generating HTML files to display scraped news data.

Functions:
- generate_html(news_data, output_file='scraped_news.html'): 
    Generates an HTML file containing a list of news articles from the provided news data.

The HTML file includes styling for a clean and organized display of news articles, 
with links that open in a new browser tab. The generated file is automatically 
opened in the default web browser.
"""
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
        <title>Scraped Election News In Ghana</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #333; }
            ul { list-style-type: none; padding: 0; }
            li { margin: 10px 0; }
            a { text-decoration: none; color: #1a73e8; }
            a:hover { text-decoration: underline; }
            .error { color: red; }
            
            .container {
                max-width: 1200px; 
                margin: 10px auto; 
                padding: 20px; 
            }
            h1 {
                text-align: center;
                margin-bottom: 20px;
            }
            .card-container {
                display: flex; 
                justify-content: center; 
                align-items: center; 
            }
            .card-list {
                display: flex;
                flex-wrap: wrap; 
                gap: 20px; 
                list-style-type: none; 
                padding: 0;
                margin: 0;
            }
            h1 {
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                padding: 16px;
                transition: transform 0.3s ease, box-shadow 0.3s ease; 
            }
            img {
                width: 50px;
                height: 50px;
            }
            .card-list li{
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                padding: 16px;
                width: calc(45.333% - 20px);
                transition: transform 0.3s ease, box-shadow 0.3s ease; 
            }
            .card-list li:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
                background-color: #d3e3fc; 
            }
            .card-list li  a {
                color: #555;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1><img src="ghana-flag.png" alt="Ghana Flag"/> Election 2024, Ghana Election News <img src="ghana-flag.png" alt="Ghana Flag"/></h1>
            <div class="card-container">
                <ul class='card-list'>
    """

    # Add the news data to the HTML content
    for news in news_data:
        if 'error' in news:
            html_content += f"<li class='error'>Error: {news['error']}</li>"
        else:
            title = news.get('title', 'No title available')
            url = news.get('url', '#')
            date = news.get('date', 'No date available')
            content = news.get('content', 'No content available')

            html_content += f"""
                <li class="news-item">
                    <div class="title"><a href="{url}" target="_blank">{title}</a></div>
                    <div class="date">Published on: {date}</div>
                    <div class="content">{content}</div>
                </li>
            """

    # Closing HTML tags
    html_content += """
                </ul>
            </div>
        </div>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    # will be replace with logger scrapper
    print(f"HTML file '{output_file}' generated successfully.")

    # Automatically open the file in the default web browser
    webbrowser.open('file://' + os.path.realpath(output_file))
