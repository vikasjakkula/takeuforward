# Step 5: Parsing XML with Python

## Introduction

Now that you understand XML structure, let's learn to parse it programmatically using Python's `xml.etree.ElementTree` module. This is Python's built-in XML parser - no additional installation needed!

## Key Methods

### Loading XML

**From a file:**
```python
import xml.etree.ElementTree as ET

tree = ET.parse('file.xml')
root = tree.getroot()
```

**From a string:**
```python
root = ET.fromstring(xml_string)
```

### Finding Elements

**Find first matching element:**
```python
book = root.find('book')  # Returns first <book> element or None
```

**Find all matching elements:**
```python
books = root.findall('book')  # Returns list of all <book> elements
```

**Find with XPath (advanced):**
```python
books = root.findall('.//book[@category="fiction"]')  # All fiction books
```

### Extracting Data

**Get text content:**
```python
title = book.find('title').text
```

**Get attributes:**
```python
book_id = book.get('id')
category = book.get('category')
```

**Get all attributes:**
```python
attrs = book.attrib  # Returns dictionary of all attributes
```

### Iterating

**Iterate through children:**
```python
for book in root:
    print(book.find('title').text)
```

**Iterate through all descendants:**
```python
for elem in root.iter():
    print(elem.tag, elem.text)
```

## Common Patterns

### Pattern 1: Extract All Items
```python
tree = ET.parse('data.xml')
root = tree.getroot()

items = []
for item in root.findall('item'):
    items.append({
        'id': item.get('id'),
        'name': item.find('name').text,
        'value': item.find('value').text
    })
```

### Pattern 2: Filter by Attribute
```python
fiction_books = []
for book in root.findall('book'):
    if book.get('category') == 'fiction':
        fiction_books.append(book.find('title').text)
```

### Pattern 3: Safe Extraction (Handle Missing)
```python
def safe_find_text(element, tag, default='N/A'):
    """Safely extract text from an element."""
    found = element.find(tag)
    return found.text if found is not None else default

title = safe_find_text(book, 'title')
```

### Pattern 4: Nested Elements
```python
# For nested structures
author = book.find('author')
author_name = author.find('name').text if author is not None else None
```

## RSS Feed Parsing

RSS feeds are a common XML format. Here's the structure:

```xml
<rss>
    <channel>
        <item>
            <title>Article Title</title>
            <link>https://example.com</link>
            <pubDate>Date</pubDate>
            <description>Content</description>
        </item>
    </channel>
</rss>
```

**Parsing pattern:**
```python
tree = ET.parse('rss.xml')
root = tree.getroot()

# RSS feeds often have namespaces
channel = root.find('channel')
for item in channel.findall('item'):
    title = item.find('title').text
    link = item.find('link').text
    pub_date = item.find('pubDate').text
```

## Handling Namespaces

Some XML uses namespaces. You need to handle them:

```python
# Define namespace
ns = {'rss': 'http://www.w3.org/2005/Atom'}

# Use in find operations
items = root.findall('rss:item', ns)
```

## Error Handling

Always handle potential errors:

```python
try:
    tree = ET.parse('file.xml')
    root = tree.getroot()
except ET.ParseError as e:
    print(f"XML parsing error: {e}")
except FileNotFoundError:
    print("File not found")
```

## Best Practices

1. **Always check for None** - `find()` returns None if element doesn't exist
2. **Use try/except** - Handle parsing errors gracefully
3. **Validate structure** - Check if expected elements exist
4. **Handle missing data** - Provide defaults for missing elements
5. **Use findall() for multiple items** - More efficient than multiple find() calls

## Next Steps

Practice with:
1. The examples in `parse_rss.py`
2. The exercises in `exercises.py`
3. Move to Step 6: XML Mini Project

---

**Tip:** Use `print(ET.tostring(element))` to see the XML representation of an element for debugging!

