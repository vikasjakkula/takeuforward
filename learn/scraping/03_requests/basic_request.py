"""
Basic HTTP Request Examples
This file demonstrates how to use the requests library to fetch web pages.
"""

import requests
import time

def example_1_simple_request():
    """Example 1: The simplest GET request"""
    print("=" * 60)
    print("Example 1: Simple GET Request")
    print("=" * 60)
    
    # Make a request to a simple website
    response = requests.get('https://httpbin.org/get')
    
    # Check the status code
    print(f"Status Code: {response.status_code}")
    
    # Print the response content (JSON in this case)
    print(f"\nResponse Content:\n{response.text[:200]}...")  # First 200 chars
    print()

def example_2_check_status():
    """Example 2: Checking status codes"""
    print("=" * 60)
    print("Example 2: Checking Status Codes")
    print("=" * 60)
    
    urls = [
        'https://httpbin.org/status/200',  # Success
        'https://httpbin.org/status/404',  # Not found
        'https://httpbin.org/status/500',  # Server error
    ]
    
    for url in urls:
        response = requests.get(url)
        status = response.status_code
        
        if status == 200:
            print(f"✓ {url} - Success!")
        elif status == 404:
            print(f"✗ {url} - Not Found")
        else:
            print(f"✗ {url} - Status: {status}")
    print()

def example_3_with_headers():
    """Example 3: Setting custom headers"""
    print("=" * 60)
    print("Example 3: Custom Headers")
    print("=" * 60)
    
    # Set a User-Agent header (identifies your program)
    headers = {
        'User-Agent': 'MyWebScraper/1.0 (Learning Web Scraping)'
    }
    
    # Make request with headers
    response = requests.get('https://httpbin.org/headers', headers=headers)
    
    # httpbin.org/headers returns the headers it received
    print("Headers sent to server:")
    print(response.text)
    print()

def example_4_error_handling():
    """Example 4: Proper error handling"""
    print("=" * 60)
    print("Example 4: Error Handling")
    print("=" * 60)
    
    urls = [
        'https://httpbin.org/get',           # This will work
        'https://httpbin.org/status/404',    # This will return 404
        'https://invalid-url-that-does-not-exist-12345.com',  # This will fail
    ]
    
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raises exception for 4xx/5xx status codes
            print(f"✓ Successfully fetched: {url}")
        except requests.exceptions.Timeout:
            print(f"✗ Timeout: {url}")
        except requests.exceptions.ConnectionError:
            print(f"✗ Connection Error: {url}")
        except requests.exceptions.HTTPError as e:
            print(f"✗ HTTP Error: {url} - {e}")
        except requests.exceptions.RequestException as e:
            print(f"✗ Request Error: {url} - {e}")
    print()

def example_5_save_to_file():
    """Example 5: Saving response to a file"""
    print("=" * 60)
    print("Example 5: Saving Response to File")
    print("=" * 60)
    
    # Fetch a simple HTML page
    response = requests.get('https://httpbin.org/html')
    
    # Save to file
    filename = '03_requests/saved_page.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    
    print(f"✓ Saved response to: {filename}")
    print(f"  Content length: {len(response.text)} characters")
    print()

def example_6_json_response():
    """Example 6: Working with JSON responses"""
    print("=" * 60)
    print("Example 6: JSON Response")
    print("=" * 60)
    
    # Fetch JSON data
    response = requests.get('https://httpbin.org/json')
    
    # Parse JSON
    data = response.json()
    
    print("Parsed JSON data:")
    print(f"  Type: {type(data)}")
    print(f"  Keys: {list(data.keys())}")
    print(f"  Sample: {str(data)[:100]}...")
    print()

def example_7_timeout():
    """Example 7: Using timeouts"""
    print("=" * 60)
    print("Example 7: Timeout Example")
    print("=" * 60)
    
    try:
        # This should work quickly
        response = requests.get('https://httpbin.org/delay/1', timeout=5)
        print(f"✓ Request completed in time: {response.status_code}")
    except requests.exceptions.Timeout:
        print("✗ Request timed out")
    
    try:
        # This will timeout (delay is 10 seconds, timeout is 2)
        response = requests.get('https://httpbin.org/delay/10', timeout=2)
        print(f"✓ Request completed: {response.status_code}")
    except requests.exceptions.Timeout:
        print("✗ Request timed out (as expected)")
    print()

def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("BASIC HTTP REQUEST EXAMPLES")
    print("=" * 60 + "\n")
    
    example_1_simple_request()
    time.sleep(0.5)  # Small delay between examples
    
    example_2_check_status()
    time.sleep(0.5)
    
    example_3_with_headers()
    time.sleep(0.5)
    
    example_4_error_handling()
    time.sleep(0.5)
    
    example_5_save_to_file()
    time.sleep(0.5)
    
    example_6_json_response()
    time.sleep(0.5)
    
    example_7_timeout()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()

