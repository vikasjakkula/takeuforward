"""
RSS Feed Parsing Example
This demonstrates how to parse RSS feed XML format.
"""

import xml.etree.ElementTree as ET
import requests

def parse_rss_from_file(filename):
    """Parse an RSS feed from a local XML file."""
    print("=" * 60)
    print("Parsing RSS Feed from File")
    print("=" * 60)
    
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # RSS feeds have a <channel> element
        channel = root.find('channel')
        
        if channel is None:
            print("Error: No <channel> element found")
            return
        
        # Get channel information
        title = channel.find('title')
        description = channel.find('description')
        
        print(f"Feed Title: {title.text if title is not None else 'N/A'}")
        print(f"Description: {description.text if description is not None else 'N/A'}")
        print()
        
        # Get all items (articles)
        items = channel.findall('item')
        print(f"Found {len(items)} articles:\n")
        
        for i, item in enumerate(items, 1):
            item_title = item.find('title')
            item_link = item.find('link')
            item_pubdate = item.find('pubDate')
            item_description = item.find('description')
            
            print(f"Article {i}:")
            print(f"  Title: {item_title.text if item_title is not None else 'N/A'}")
            print(f"  Link: {item_link.text if item_link is not None else 'N/A'}")
            print(f"  Published: {item_pubdate.text if item_pubdate is not None else 'N/A'}")
            
            # Description might be long, show first 100 chars
            if item_description is not None and item_description.text:
                desc = item_description.text[:100]
                print(f"  Description: {desc}...")
            print()
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"Error: {e}")

def parse_rss_from_url(url):
    """Parse an RSS feed from a URL."""
    print("=" * 60)
    print("Parsing RSS Feed from URL")
    print("=" * 60)
    
    try:
        # Fetch the RSS feed
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse the XML
        root = ET.fromstring(response.content)
        
        # RSS feeds have a <channel> element
        channel = root.find('channel')
        
        if channel is None:
            print("Error: No <channel> element found")
            return
        
        # Get channel information
        title = channel.find('title')
        print(f"Feed Title: {title.text if title is not None else 'N/A'}")
        print()
        
        # Get all items
        items = channel.findall('item')
        print(f"Found {len(items)} articles:\n")
        
        # Show first 3 articles
        for i, item in enumerate(items[:3], 1):
            item_title = item.find('title')
            item_link = item.find('link')
            
            print(f"Article {i}:")
            print(f"  Title: {item_title.text if item_title is not None else 'N/A'}")
            print(f"  Link: {item_link.text if item_link is not None else 'N/A'}")
            print()
        
        if len(items) > 3:
            print(f"... and {len(items) - 3} more articles")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"Error: {e}")

def extract_rss_data(filename):
    """Extract RSS data into a structured format (list of dictionaries)."""
    print("=" * 60)
    print("Extracting RSS Data to Structured Format")
    print("=" * 60)
    
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        channel = root.find('channel')
        
        if channel is None:
            print("Error: No <channel> element found")
            return []
        
        articles = []
        
        for item in channel.findall('item'):
            article = {
                'title': safe_get_text(item, 'title'),
                'link': safe_get_text(item, 'link'),
                'pubDate': safe_get_text(item, 'pubDate'),
                'description': safe_get_text(item, 'description'),
            }
            articles.append(article)
        
        # Display results
        print(f"Extracted {len(articles)} articles:\n")
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
            print(f"   Link: {article['link']}")
            print(f"   Date: {article['pubDate']}")
            print()
        
        return articles
        
    except Exception as e:
        print(f"Error: {e}")
        return []

def safe_get_text(element, tag, default='N/A'):
    """Safely get text from an XML element."""
    found = element.find(tag)
    return found.text if found is not None and found.text else default

def main():
    """Run RSS parsing examples."""
    print("\n" + "=" * 60)
    print("RSS FEED PARSING EXAMPLES")
    print("=" * 60 + "\n")
    
    # Example 1: Parse from file (use the test RSS file from step 6)
    # Uncomment when you have the test file:
    # parse_rss_from_file('06_xml_project/test_rss.xml')
    
    # Example 2: Parse from URL (uncomment to try a real RSS feed)
    # Note: Some RSS feeds may be blocked or require specific headers
    # parse_rss_from_url('https://feeds.bbci.co.uk/news/rss.xml')
    
    print("\n" + "=" * 60)
    print("To test RSS parsing:")
    print("1. Create a test RSS file (see Step 6)")
    print("2. Uncomment the parse_rss_from_file() call above")
    print("=" * 60)

if __name__ == "__main__":
    main()

