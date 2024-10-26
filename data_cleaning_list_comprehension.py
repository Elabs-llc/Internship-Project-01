from typing import List, Dict, Any
from datetime import datetime
import re


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

    def clean_articles(self, raw_articles: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Clean article data using list comprehensions.

        Args:
            raw_articles: List of raw article dictionaries

        Returns:
            List of cleaned article dictionaries
        """
        return [
            {
                'title': self.clean_text(article.get('title', '')),
                'content': self.clean_text(article.get('content', '')),
                'date': self.normalize_date(article.get('date', '')),
                'url': article.get('url', ''),
                'election_related': self.is_election_related(article.get('content', '')),
                'regions_mentioned': self.extract_regions(article.get('content', '')),
                'parties_mentioned': self.extract_parties(article.get('content', ''))
            }
            for article in raw_articles
            if article and article.get('content')
        ]

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


def main():
    # Example
    cleaner = ElectionDataCleaner()

    # Sample raw articles (from the web scraping from earlier)
    raw_articles = [
        {
            'title': 'Election Update: NPP Rally in Ashanti Region',
            'content': 'The New Patriotic Party held a rally in Kumasi, Ashanti Region. About 15,000 votes expected.',
            'date': 'January 15, 2024',
            'url': 'https://example.com/article1'
        },
        {
            'title': 'EC Announces Polling Stations',
            'content': 'Electoral Commission announces 25% increase in polling stations across Greater Accra.',
            'date': '15-01-2024',
            'url': 'https://example.com/article2'
        }
    ]

    # Clean and process articles
    cleaned_articles = cleaner.clean_articles(raw_articles)
    election_articles = cleaner.filter_election_articles(cleaned_articles)
    stats = cleaner.analyze_article_statistics(cleaned_articles)

    # Example of accessing results
    for article in election_articles:
        print(f"\nTitle: {article['title']}")
        print(f"Date: {article['date']}")
        print(f"Regions: {', '.join(article['regions_mentioned'])}")
        print(f"Parties: {', '.join(article['parties_mentioned'])}")


if __name__ == "__main__":
    main()
