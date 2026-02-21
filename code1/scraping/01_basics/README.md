# Step 1: Understanding Web Scraping Basics

## What is Web Scraping?

Web scraping is the process of automatically extracting data from websites. Instead of manually copying information, you write code that:
- Fetches web pages
- Parses the content (HTML/XML)
- Extracts specific information
- Saves it in a structured format (JSON, CSV, database)

## When to Use Web Scraping?

✅ **Good use cases:**
- Collecting product prices for comparison
- Gathering news articles from RSS feeds
- Extracting data for research
- Monitoring website changes
- Building datasets for machine learning
- Aggregating information from multiple sources

❌ **Avoid when:**
- The website provides an official API
- The data is available in a downloadable format
- Terms of Service prohibit scraping
- You need real-time data (APIs are better)

## HTML vs XML

### HTML (HyperText Markup Language)
- Used for displaying web pages in browsers
- Structure: `<tag>content</tag>` with attributes
- Example: `<div class="product">Product Name</div>`
- Less strict - browsers are forgiving of errors
- Designed for human-readable web pages

### XML (eXtensible Markup Language)
- Used for data storage and exchange
- Structure: Similar to HTML but stricter
- Example: `<item><title>Article</title></item>`
- Must be well-formed (no errors allowed)
- Designed for data exchange between systems
- Common formats: RSS feeds, API responses, configuration files

## HTTP Requests

When you visit a website, your browser sends an **HTTP request** to the server:

### GET Request
- Most common type
- Used to retrieve data
- Example: Visiting a webpage, fetching an RSS feed
- No data sent in the request body

### POST Request
- Used to send data to the server
- Example: Submitting a form, logging in
- Data sent in the request body

### HTTP Status Codes
- **200 OK**: Request successful
- **404 Not Found**: Page doesn't exist
- **403 Forbidden**: Access denied
- **500 Server Error**: Server problem
- **429 Too Many Requests**: Rate limited

## Web Page Structure

### HTML Tags
HTML uses tags to structure content:
```html
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <h1>Heading</h1>
    <p>Paragraph text</p>
    <div class="container">
      <a href="https://example.com">Link</a>
    </div>
  </body>
</html>
```

### DOM (Document Object Model)
- The browser creates a tree structure of the HTML
- Each tag becomes a "node" in the tree
- You can navigate: parent → children → siblings
- This is what web scrapers parse!

## Legal and Ethical Considerations

### ✅ Always Do:
- Check the website's `robots.txt` file
- Read the Terms of Service
- Respect rate limits (don't overload servers)
- Use appropriate delays between requests
- Identify yourself with a User-Agent header
- Only scrape publicly available data

### ❌ Never Do:
- Scrape personal data without permission
- Violate copyright laws
- Overload servers with too many requests
- Scrape behind authentication without permission
- Ignore robots.txt directives

### robots.txt
Located at `https://example.com/robots.txt`, this file tells scrapers what they can and cannot access.

Example:
```
User-agent: *
Allow: /public/
Disallow: /private/
Crawl-delay: 10
```

## Key Concepts Summary

1. **Web Scraping** = Automatically extracting data from websites
2. **HTML** = Structure of web pages (visual content)
3. **XML** = Structured data format (RSS, APIs)
4. **HTTP Requests** = How you fetch web pages
5. **DOM** = Tree structure of HTML elements
6. **Ethics** = Always respect websites and their rules

## Next Steps

Now that you understand the basics, you're ready to:
1. Set up your Python environment (Step 2)
2. Learn to make HTTP requests (Step 3)
3. Start scraping XML data (Step 4)

---

**Take your time with this step!** Understanding these fundamentals will make everything else much easier.

