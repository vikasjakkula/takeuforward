# Step 3: Making HTTP Requests

## Introduction

The `requests` library is the foundation of web scraping. It allows you to fetch web pages, just like a browser does, but programmatically.

## Basic GET Request

The simplest way to fetch a webpage:

```python
import requests

response = requests.get('https://example.com')
print(response.text)  # The HTML content
```

## Understanding the Response Object

When you make a request, you get a `Response` object with useful information:

### Status Code
```python
response = requests.get('https://example.com')
print(response.status_code)  # 200 means success
```

Common status codes:
- **200**: OK - Request successful
- **404**: Not Found - Page doesn't exist
- **403**: Forbidden - Access denied
- **500**: Internal Server Error - Server problem
- **429**: Too Many Requests - You're making requests too fast

### Response Content
```python
response.text      # HTML/XML as a string
response.content   # Raw bytes
response.json()    # If response is JSON (will raise error if not JSON)
```

### Headers
```python
response.headers   # Response headers (dictionary)
response.headers['Content-Type']  # e.g., 'text/html'
```

## Error Handling

Always handle errors when making requests:

```python
import requests

try:
    response = requests.get('https://example.com')
    response.raise_for_status()  # Raises exception for bad status codes
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

## Setting Headers

Some websites block requests without proper headers. Always set a User-Agent:

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get('https://example.com', headers=headers)
```

## Timeouts

Always set timeouts to avoid hanging:

```python
# Timeout after 5 seconds
response = requests.get('https://example.com', timeout=5)
```

## Common Patterns

### Check if request succeeded
```python
if response.status_code == 200:
    print("Success!")
else:
    print(f"Failed with status: {response.status_code}")
```

### Get JSON data
```python
response = requests.get('https://api.example.com/data')
data = response.json()  # Automatically parses JSON
```

### Save response to file
```python
response = requests.get('https://example.com')
with open('page.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
```

## Best Practices

1. **Always use timeouts** - Don't let requests hang forever
2. **Set User-Agent** - Identify yourself to servers
3. **Handle errors** - Use try/except blocks
4. **Check status codes** - Verify the request succeeded
5. **Respect rate limits** - Add delays between requests
6. **Use sessions** - For multiple requests to the same site

## Rate Limiting

Be respectful! Add delays between requests:

```python
import time

for url in urls:
    response = requests.get(url)
    time.sleep(1)  # Wait 1 second between requests
```

## Next Steps

Now you can:
1. Practice with the exercises in `request_exercises.py`
2. Move to Step 4: Understanding XML Structure
3. Start scraping real data!

---

**Remember:** Web scraping is about being respectful. Don't overload servers with too many requests!

