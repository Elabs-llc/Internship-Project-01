from typing import List, Dict, Any
from datetime import datetime
import re

from logs import log_execution_time, log_message


class ElectionDataCleaner:
    def __init__(self):
        # Keywords for filtering election-related content
        self.election_keywords = [
            'election', 'vote', 'ballot', 'polling',
            'EC', 'Electoral Commission', 'constituency',
            'candidate', 'NPP', 'NDC', 'campaign'
        ]

        # Ghana's political parties (we can add the rest)
        self.political_parties = {
            'NPP': 'New Patriotic Party',
            'NDC': 'National Democratic Congress',
            'CPP': "Convention People's Party",
            'PPP': "Progressive People's Party"
        }

        # Ghana's regions
        self.regions = [
            'Greater Accra', 'Ashanti', 'Central', 'Eastern',
            'Western', 'Volta', 'Northern', 'Upper East',
            'Upper West', 'Bono', 'Ahafo', 'Bono East',
            'North East', 'Savannah', 'Oti', 'Western North'
        ]

    # Log message & execution time
    @log_message(message='New article cleaned successfully')
    @log_execution_time
    def clean_articles(self, raw_articles: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Clean article data using list comprehensions.

        Args:
            raw_articles: List of raw article dictionaries

        Returns:
            List of cleaned article dictionaries
        """
        cleaned_articles = []
        for article in raw_articles:
            if not article or not article.get('title'):
                continue

            cleaned_article = {
                'title': self.clean_text(article.get('title', '')),
                'content': self.clean_text(article.get('content', '')),
                'date': self.normalize_date(article.get('date', '')),
                'url': article.get('url', ''),
                'election_related': self.is_election_related(article.get('content', '')),
                'regions_mentioned': self.extract_regions(article.get('content', '')),
                'parties_mentioned': self.extract_parties(article.get('content', ''))
            }

            # Add additional checks or debugging here, e.g.: | will be log using logger module
            # if not cleaned_article['election_related']:
            #     print(f"Article not election-related: {cleaned_article['title']}")
            # if not cleaned_article['regions_mentioned'] and not cleaned_article['parties_mentioned']:
            #     print(f"No regions or parties mentioned: {cleaned_article['title']}")

            cleaned_articles.append(cleaned_article)

        return cleaned_articles

    # Log message & execution time
    @log_message(message='HTML tags, special characters, and normalizes whitespace removed from news')
    @log_execution_time
    def clean_text(self, text: str) -> str:
        """
        Clean text using list comprehension.
        Removes HTML tags, special characters, and normalizes whitespace.
        """
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)

        # Split into words and clean each word
        words = text.split()
        cleaned_words = [
            ''.join(char for char in word if char.isalnum() or char in "'-,.")
            for word in words
        ]

        # Join cleaned words, removing empty strings
        return ' '.join(word for word in cleaned_words if word)

    # Log message & execution time
    @log_message(message='date formats normalized')
    @log_execution_time
    def normalize_date(self, date_str: str) -> str:
        """Normalize date formats using list comprehension for pattern matching"""
        # Common date formats found in Ghana news websites
        date_patterns = [
            '%B %d, %Y',  # December 25, 2024
            '%d-%m-%Y',  # 25-12-2024
            '%Y-%m-%d',  # 2024-12-25
            '%d/%m/%Y',  # 25/12/2024
            '%d %B %Y'  # 25 December 2024
        ]

        # Try each pattern until one works
        for pattern in date_patterns:
            try:
                return datetime.strptime(date_str.strip(), pattern).strftime('%Y-%m-%d')
            except ValueError:
                continue
        return date_str


    def is_election_related(self, content: str) -> bool:
        """Check if content is election-related using list comprehension"""
        return any(
            keyword.lower() in content.lower()
            for keyword in self.election_keywords
        )

    def extract_regions(self, content: str) -> List[str]:
        """Extract mentioned regions using list comprehension"""
        return [
            region for region in self.regions
            if region.lower() in content.lower()
        ]

    def extract_parties(self, content: str) -> List[str]:
        """Extract mentioned political parties using list comprehension"""
        return [
            full_name for abbr, full_name in self.political_parties.items()
            if abbr in content or full_name in content
        ]

    def extract_statistics(self, content: str) -> Dict[str, List[str]]:
        """Extract electoral statistics using list comprehension"""
        return {
            'percentages': [
                match for match in re.findall(r'\d+(?:\.\d+)?%', content)
            ],
            'vote_counts': [
                match for match in re.findall(r'\b\d{1,3}(?:,\d{3})*\s+votes?\b', content)
            ]
        }

    def filter_election_articles(self, articles: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Filter election-related articles using list comprehension"""
        return [
            article for article in articles
            if article['election_related'] and (
                    article['regions_mentioned'] or
                    article['parties_mentioned']
            )
        ]

    def analyze_article_statistics(self, articles: List[Dict[str, str]]) -> Dict[str, Any]:
        """Analyze article statistics using list comprehensions"""
        return {
            'total_articles': len(articles),
            'election_related': len([a for a in articles if a['election_related']]),
            'regions_coverage': {
                region: len([
                    a for a in articles
                    if region in a['regions_mentioned']
                ])
                for region in self.regions
            },
            'party_mentions': {
                party: len([
                    a for a in articles
                    if party in a['parties_mentioned']
                ])
                for party in self.political_parties.values()
            }
        }

