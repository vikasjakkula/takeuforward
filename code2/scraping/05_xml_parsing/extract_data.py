"""
Extracting Specific Data from XML
This demonstrates various techniques for extracting data from XML files.
"""

import xml.etree.ElementTree as ET
import json

def extract_all_books():
    """Extract all books from the library XML into a list of dictionaries."""
    print("=" * 60)
    print("Extracting All Books")
    print("=" * 60)
    
    try:
        tree = ET.parse('04_xml_basics/xml_example.xml')
        root = tree.getroot()
        
        books = []
        
        for book in root.findall('book'):
            book_data = {
                'id': book.get('id'),
                'category': book.get('category'),
                'available': book.get('available'),
                'title': safe_get_text(book, 'title'),
                'author': safe_get_text(book, 'author'),
                'year': safe_get_text(book, 'year'),
                'price': safe_get_text(book, 'price'),
                'currency': book.find('price').get('currency') if book.find('price') is not None else None,
                'description': safe_get_text(book, 'description'),
                'isbn': safe_get_text(book, 'isbn'),
            }
            books.append(book_data)
        
        # Display results
        print(f"Extracted {len(books)} books:\n")
        for book in books:
            print(f"Title: {book['title']}")
            print(f"  Author: {book['author']}")
            print(f"  Price: ${book['price']} ({book['currency']})")
            print(f"  Available: {book['available']}")
            print()
        
        return books
        
    except FileNotFoundError:
        print("Error: xml_example.xml not found")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def filter_by_category(category):
    """Extract books filtered by category."""
    print("=" * 60)
    print(f"Filtering Books by Category: {category}")
    print("=" * 60)
    
    try:
        tree = ET.parse('04_xml_basics/xml_example.xml')
        root = tree.getroot()
        
        filtered_books = []
        
        for book in root.findall('book'):
            if book.get('category') == category:
                book_data = {
                    'title': safe_get_text(book, 'title'),
                    'author': safe_get_text(book, 'author'),
                    'year': safe_get_text(book, 'year'),
                }
                filtered_books.append(book_data)
        
        print(f"Found {len(filtered_books)} {category} books:\n")
        for book in filtered_books:
            print(f"- {book['title']} by {book['author']} ({book['year']})")
        print()
        
        return filtered_books
        
    except Exception as e:
        print(f"Error: {e}")
        return []

def extract_available_books():
    """Extract only available books."""
    print("=" * 60)
    print("Extracting Available Books")
    print("=" * 60)
    
    try:
        tree = ET.parse('04_xml_basics/xml_example.xml')
        root = tree.getroot()
        
        available_books = []
        
        for book in root.findall('book'):
            if book.get('available') == 'true':
                available_books.append({
                    'title': safe_get_text(book, 'title'),
                    'price': safe_get_text(book, 'price'),
                    'currency': book.find('price').get('currency') if book.find('price') is not None else None,
                })
        
        print(f"Found {len(available_books)} available books:\n")
        for book in available_books:
            currency = book['currency'] or 'USD'
            print(f"- {book['title']}: ${book['price']} {currency}")
        print()
        
        return available_books
        
    except Exception as e:
        print(f"Error: {e}")
        return []

def save_to_json(filename='extracted_books.json'):
    """Extract all books and save to JSON file."""
    print("=" * 60)
    print("Saving Extracted Data to JSON")
    print("=" * 60)
    
    try:
        tree = ET.parse('04_xml_basics/xml_example.xml')
        root = tree.getroot()
        
        books = []
        
        for book in root.findall('book'):
            book_data = {
                'id': int(book.get('id')),  # Convert to integer
                'category': book.get('category'),
                'available': book.get('available') == 'true',  # Convert to boolean
                'title': safe_get_text(book, 'title'),
                'author': safe_get_text(book, 'author'),
                'year': int(safe_get_text(book, 'year', '0')),  # Convert to integer
                'price': float(safe_get_text(book, 'price', '0')),  # Convert to float
                'currency': book.find('price').get('currency') if book.find('price') is not None else 'USD',
                'description': safe_get_text(book, 'description'),
                'isbn': safe_get_text(book, 'isbn'),
            }
            books.append(book_data)
        
        # Save to JSON
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(books, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Saved {len(books)} books to {filename}")
        print()
        
        return books
        
    except Exception as e:
        print(f"Error: {e}")
        return []

def extract_statistics():
    """Extract statistics from the XML data."""
    print("=" * 60)
    print("Extracting Statistics")
    print("=" * 60)
    
    try:
        tree = ET.parse('04_xml_basics/xml_example.xml')
        root = tree.getroot()
        
        total_books = len(root.findall('book'))
        available_count = 0
        categories = {}
        total_price = 0.0
        
        for book in root.findall('book'):
            # Count available
            if book.get('available') == 'true':
                available_count += 1
            
            # Count by category
            category = book.get('category')
            categories[category] = categories.get(category, 0) + 1
            
            # Sum prices
            price_elem = book.find('price')
            if price_elem is not None and price_elem.text:
                total_price += float(price_elem.text)
        
        print(f"Total books: {total_books}")
        print(f"Available books: {available_count}")
        print(f"Unavailable books: {total_books - available_count}")
        print(f"\nBooks by category:")
        for category, count in categories.items():
            print(f"  {category}: {count}")
        print(f"\nTotal value: ${total_price:.2f}")
        print(f"Average price: ${total_price/total_books:.2f}")
        print()
        
    except Exception as e:
        print(f"Error: {e}")

def safe_get_text(element, tag, default='N/A'):
    """Safely get text from an XML element."""
    found = element.find(tag)
    return found.text if found is not None and found.text else default

def main():
    """Run all extraction examples."""
    print("\n" + "=" * 60)
    print("XML DATA EXTRACTION EXAMPLES")
    print("=" * 60 + "\n")
    
    extract_all_books()
    filter_by_category('fiction')
    extract_available_books()
    save_to_json('05_xml_parsing/extracted_books.json')
    extract_statistics()
    
    print("=" * 60)
    print("All extraction examples completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()

