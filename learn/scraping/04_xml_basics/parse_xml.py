"""
Basic XML Parsing Examples
This file demonstrates how to parse XML using Python's built-in xml.etree.ElementTree module.
"""

import xml.etree.ElementTree as ET

def example_1_load_xml():
    """Example 1: Loading and parsing an XML file"""
    print("=" * 60)
    print("Example 1: Loading XML File")
    print("=" * 60)
    
    # Parse the XML file
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    
    # Print the root element tag
    print(f"Root element: {root.tag}")
    print(f"Number of books: {len(root)}")
    print()

def example_2_iterate_elements():
    """Example 2: Iterating through XML elements"""
    print("=" * 60)
    print("Example 2: Iterating Through Elements")
    print("=" * 60)
    
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    
    # Iterate through all book elements
    for book in root.findall('book'):
        print(f"Found book: {book.get('id')}")
    print()

def example_3_extract_text():
    """Example 3: Extracting text content from elements"""
    print("=" * 60)
    print("Example 3: Extracting Text Content")
    print("=" * 60)
    
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    
    # Get the first book
    first_book = root.find('book')
    
    if first_book is not None:
        title = first_book.find('title').text
        author = first_book.find('author').text
        year = first_book.find('year').text
        
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Year: {year}")
    print()

def example_4_extract_attributes():
    """Example 4: Extracting attributes from elements"""
    print("=" * 60)
    print("Example 4: Extracting Attributes")
    print("=" * 60)
    
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    
    # Get attributes from the first book
    first_book = root.find('book')
    
    if first_book is not None:
        book_id = first_book.get('id')
        category = first_book.get('category')
        available = first_book.get('available')
        
        print(f"Book ID: {book_id}")
        print(f"Category: {category}")
        print(f"Available: {available}")
    print()

def example_5_all_books():
    """Example 5: Extracting all books with their details"""
    print("=" * 60)
    print("Example 5: All Books Information")
    print("=" * 60)
    
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    
    # Iterate through all books
    for book in root.findall('book'):
        print(f"\nBook ID: {book.get('id')}")
        print(f"  Title: {book.find('title').text}")
        print(f"  Author: {book.find('author').text}")
        print(f"  Year: {book.find('year').text}")
        print(f"  Price: ${book.find('price').text} ({book.find('price').get('currency')})")
        print(f"  Available: {book.get('available')}")
    print()

def example_6_find_specific():
    """Example 6: Finding specific elements"""
    print("=" * 60)
    print("Example 6: Finding Specific Elements")
    print("=" * 60)
    
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    
    # Find all fiction books
    print("Fiction books:")
    for book in root.findall('book'):
        if book.get('category') == 'fiction':
            print(f"  - {book.find('title').text}")
    
    # Find all available books
    print("\nAvailable books:")
    for book in root.findall('book'):
        if book.get('available') == 'true':
            print(f"  - {book.find('title').text}")
    print()

def example_7_handle_missing():
    """Example 7: Handling missing elements safely"""
    print("=" * 60)
    print("Example 7: Handling Missing Elements")
    print("=" * 60)
    
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    
    first_book = root.find('book')
    
    if first_book is not None:
        # Safe way to get text (returns None if element doesn't exist)
        title_elem = first_book.find('title')
        title = title_elem.text if title_elem is not None else "N/A"
        
        # Try to find a non-existent element
        subtitle_elem = first_book.find('subtitle')
        subtitle = subtitle_elem.text if subtitle_elem is not None else "No subtitle"
        
        print(f"Title: {title}")
        print(f"Subtitle: {subtitle}")
    print()

def example_8_xml_from_string():
    """Example 8: Parsing XML from a string"""
    print("=" * 60)
    print("Example 8: Parsing XML from String")
    print("=" * 60)
    
    # XML as a string
    xml_string = '''<?xml version="1.0"?>
    <data>
        <item id="1">First Item</item>
        <item id="2">Second Item</item>
    </data>'''
    
    # Parse from string
    root = ET.fromstring(xml_string)
    
    print(f"Root: {root.tag}")
    for item in root.findall('item'):
        print(f"  {item.get('id')}: {item.text}")
    print()

def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("BASIC XML PARSING EXAMPLES")
    print("=" * 60 + "\n")
    
    try:
        example_1_load_xml()
        example_2_iterate_elements()
        example_3_extract_text()
        example_4_extract_attributes()
        example_5_all_books()
        example_6_find_specific()
        example_7_handle_missing()
        example_8_xml_from_string()
        
        print("=" * 60)
        print("All examples completed!")
        print("=" * 60)
    except FileNotFoundError:
        print("Error: xml_example.xml not found!")
        print("Make sure you're running this from the project root directory.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

