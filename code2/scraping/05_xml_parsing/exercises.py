"""
Practice Exercises for XML Parsing
Complete these exercises to master XML parsing with Python.
"""

import xml.etree.ElementTree as ET
import json

# ============================================================================
# EXERCISE 1: Load and Display Root
# ============================================================================
def exercise_1():
    """
    Task: Load '04_xml_basics/xml_example.xml' and print the root element tag.
    """
    print("Exercise 1: Load XML and Display Root")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Parse the XML file
    # 2. Get the root element
    # 3. Print the root tag
    
    print()

# ============================================================================
# EXERCISE 2: Count Elements
# ============================================================================
def exercise_2():
    """
    Task: Count how many <book> elements are in the XML file.
    Print the count.
    """
    print("Exercise 2: Count Book Elements")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Parse the XML file
    # 2. Find all 'book' elements
    # 3. Print the count
    
    print()

# ============================================================================
# EXERCISE 3: Extract All Titles
# ============================================================================
def exercise_3():
    """
    Task: Extract and print all book titles from the XML file.
    """
    print("Exercise 3: Extract All Titles")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Parse the XML file
    # 2. Loop through all books
    # 3. Extract and print each title
    
    print()

# ============================================================================
# EXERCISE 4: Find by Attribute
# ============================================================================
def exercise_4():
    """
    Task: Find all books where category="fiction" and print their titles.
    """
    print("Exercise 4: Find Fiction Books")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Parse the XML file
    # 2. Loop through all books
    # 3. Check if category attribute equals "fiction"
    # 4. Print the title if it matches
    
    print()

# ============================================================================
# EXERCISE 5: Extract Book Details
# ============================================================================
def exercise_5():
    """
    Task: Extract title, author, and year for each book and print them.
    Format: "Title by Author (Year)"
    """
    print("Exercise 5: Extract Book Details")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Parse the XML file
    # 2. For each book, extract title, author, year
    # 3. Print in the format: "Title by Author (Year)"
    
    print()

# ============================================================================
# EXERCISE 6: Safe Extraction
# ============================================================================
def exercise_6():
    """
    Task: Extract the ISBN for each book, but handle cases where ISBN might not exist.
    Print "No ISBN" if the element is missing.
    """
    print("Exercise 6: Safe Extraction")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Parse the XML file
    # 2. For each book, try to extract ISBN
    # 3. If ISBN doesn't exist, print "No ISBN"
    # 4. Use safe extraction (check for None)
    
    print()

# ============================================================================
# EXERCISE 7: Create Dictionary
# ============================================================================
def exercise_7():
    """
    Task: Create a list of dictionaries, where each dictionary contains:
    - title
    - author
    - year
    - category (from attribute)
    Print the list.
    """
    print("Exercise 7: Create Dictionary")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Parse the XML file
    # 2. Create an empty list
    # 3. For each book, create a dictionary with the required fields
    # 4. Append to the list
    # 5. Print the list
    
    print()

# ============================================================================
# EXERCISE 8: Save to JSON
# ============================================================================
def exercise_8():
    """
    Task: Extract all books into a list of dictionaries and save to a JSON file.
    Include: id, title, author, year, price
    """
    print("Exercise 8: Save to JSON")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Parse the XML file
    # 2. Create list of dictionaries with book data
    # 3. Use json.dump() to save to a file
    # 4. Print confirmation message
    
    print()

# ============================================================================
# EXERCISE 9: Calculate Statistics
# ============================================================================
def exercise_9():
    """
    Task: Calculate and print:
    - Total number of books
    - Number of available books
    - Average price of all books
    """
    print("Exercise 9: Calculate Statistics")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Parse the XML file
    # 2. Count total books
    # 3. Count available books (check 'available' attribute)
    # 4. Calculate average price (sum all prices, divide by count)
    # 5. Print the statistics
    
    print()

# ============================================================================
# EXERCISE 10: Filter and Extract
# ============================================================================
def exercise_10():
    """
    Task: Find all books published after 1950 and print their titles and years.
    """
    print("Exercise 10: Filter by Year")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Parse the XML file
    # 2. For each book, extract the year
    # 3. Convert year to integer and check if > 1950
    # 4. Print title and year for matching books
    
    print()

# ============================================================================
# SOLUTIONS (Uncomment to see answers)
# ============================================================================
"""
# SOLUTION 1
def exercise_1_solution():
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    print(f"Root element: {root.tag}")

# SOLUTION 2
def exercise_2_solution():
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    books = root.findall('book')
    print(f"Total books: {len(books)}")

# SOLUTION 3
def exercise_3_solution():
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    for book in root.findall('book'):
        title = book.find('title')
        if title is not None:
            print(title.text)

# SOLUTION 4
def exercise_4_solution():
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    for book in root.findall('book'):
        if book.get('category') == 'fiction':
            title = book.find('title')
            if title is not None:
                print(title.text)

# SOLUTION 5
def exercise_5_solution():
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    for book in root.findall('book'):
        title = book.find('title').text if book.find('title') is not None else 'N/A'
        author = book.find('author').text if book.find('author') is not None else 'N/A'
        year = book.find('year').text if book.find('year') is not None else 'N/A'
        print(f"{title} by {author} ({year})")

# SOLUTION 6
def exercise_6_solution():
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    for book in root.findall('book'):
        isbn_elem = book.find('isbn')
        if isbn_elem is not None and isbn_elem.text:
            print(f"ISBN: {isbn_elem.text}")
        else:
            print("No ISBN")

# SOLUTION 7
def exercise_7_solution():
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    books_list = []
    for book in root.findall('book'):
        book_dict = {
            'title': book.find('title').text if book.find('title') is not None else None,
            'author': book.find('author').text if book.find('author') is not None else None,
            'year': book.find('year').text if book.find('year') is not None else None,
            'category': book.get('category')
        }
        books_list.append(book_dict)
    print(books_list)

# SOLUTION 8
def exercise_8_solution():
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    books = []
    for book in root.findall('book'):
        books.append({
            'id': book.get('id'),
            'title': book.find('title').text if book.find('title') is not None else None,
            'author': book.find('author').text if book.find('author') is not None else None,
            'year': book.find('year').text if book.find('year') is not None else None,
            'price': book.find('price').text if book.find('price') is not None else None,
        })
    with open('exercise_output.json', 'w') as f:
        json.dump(books, f, indent=2)
    print("Saved to exercise_output.json")

# SOLUTION 9
def exercise_9_solution():
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    books = root.findall('book')
    total = len(books)
    available = sum(1 for book in books if book.get('available') == 'true')
    prices = [float(book.find('price').text) for book in books if book.find('price') is not None and book.find('price').text]
    avg_price = sum(prices) / len(prices) if prices else 0
    print(f"Total books: {total}")
    print(f"Available books: {available}")
    print(f"Average price: ${avg_price:.2f}")

# SOLUTION 10
def exercise_10_solution():
    tree = ET.parse('04_xml_basics/xml_example.xml')
    root = tree.getroot()
    for book in root.findall('book'):
        year_elem = book.find('year')
        if year_elem is not None and year_elem.text:
            year = int(year_elem.text)
            if year > 1950:
                title = book.find('title').text if book.find('title') is not None else 'N/A'
                print(f"{title} ({year})")
"""

def main():
    """Run all exercises"""
    print("\n" + "=" * 60)
    print("XML PARSING EXERCISES")
    print("=" * 60 + "\n")
    print("Complete each exercise function above.\n")
    print("Uncomment the function calls below to test your solutions:\n")
    
    # Uncomment these as you complete each exercise:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # exercise_5()
    # exercise_6()
    # exercise_7()
    # exercise_8()
    # exercise_9()
    # exercise_10()
    
    print("=" * 60)
    print("Good luck! Check the solutions at the bottom of this file if stuck.")
    print("=" * 60)

if __name__ == "__main__":
    main()

