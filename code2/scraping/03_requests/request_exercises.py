"""
Practice Exercises for HTTP Requests
Complete these exercises to master the requests library.
"""

import requests
import json

# ============================================================================
# EXERCISE 1: Basic Request
# ============================================================================
def exercise_1():
    """
    Task: Make a GET request to https://httpbin.org/get
    Print the status code and the response text.
    """
    print("Exercise 1: Basic Request")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Make a GET request to 'https://httpbin.org/get'
    # 2. Print the status code
    # 3. Print the response text
    
    print()

# ============================================================================
# EXERCISE 2: Check Status Code
# ============================================================================
def exercise_2():
    """
    Task: Make requests to these URLs and print whether each was successful:
    - https://httpbin.org/status/200
    - https://httpbin.org/status/404
    - https://httpbin.org/status/500
    
    Print "Success" for 200, "Failed" for others.
    """
    print("Exercise 2: Check Status Codes")
    print("-" * 40)
    
    urls = [
        'https://httpbin.org/status/200',
        'https://httpbin.org/status/404',
        'https://httpbin.org/status/500',
    ]
    
    # TODO: Your code here
    # Loop through each URL, make a request, and print Success/Failed
    
    print()

# ============================================================================
# EXERCISE 3: Set Headers
# ============================================================================
def exercise_3():
    """
    Task: Make a request to https://httpbin.org/headers with a custom
    User-Agent header. Print the response to see your header was sent.
    """
    print("Exercise 3: Custom Headers")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Create a headers dictionary with 'User-Agent' key
    # 2. Make a request with those headers
    # 3. Print the response text
    
    print()

# ============================================================================
# EXERCISE 4: Error Handling
# ============================================================================
def exercise_4():
    """
    Task: Make a request with proper error handling.
    Try to fetch: https://httpbin.org/status/404
    Use try/except to catch HTTPError and print a friendly message.
    """
    print("Exercise 4: Error Handling")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Use try/except block
    # 2. Make request to 'https://httpbin.org/status/404'
    # 3. Use response.raise_for_status()
    # 4. Catch requests.exceptions.HTTPError
    # 5. Print a friendly error message
    
    print()

# ============================================================================
# EXERCISE 5: Parse JSON
# ============================================================================
def exercise_5():
    """
    Task: Fetch JSON from https://httpbin.org/json
    Parse it and print the 'slideshow' title.
    """
    print("Exercise 5: Parse JSON")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Make request to 'https://httpbin.org/json'
    # 2. Parse JSON using response.json()
    # 3. Access the 'slideshow' -> 'title' and print it
    
    print()

# ============================================================================
# EXERCISE 6: Save to File
# ============================================================================
def exercise_6():
    """
    Task: Fetch HTML from https://httpbin.org/html
    Save it to a file called 'exercise_output.html'
    """
    print("Exercise 6: Save to File")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Make request to 'https://httpbin.org/html'
    # 2. Open a file 'exercise_output.html' in write mode
    # 3. Write the response text to the file
    # 4. Print confirmation message
    
    print()

# ============================================================================
# EXERCISE 7: Timeout
# ============================================================================
def exercise_7():
    """
    Task: Make a request with a 2-second timeout.
    Try: https://httpbin.org/delay/5 (this takes 5 seconds)
    Catch the timeout exception and print a message.
    """
    print("Exercise 7: Timeout")
    print("-" * 40)
    
    # TODO: Your code here
    # 1. Make request to 'https://httpbin.org/delay/5' with timeout=2
    # 2. Catch requests.exceptions.Timeout
    # 3. Print "Request timed out!"
    
    print()

# ============================================================================
# EXERCISE 8: Multiple Requests
# ============================================================================
def exercise_8():
    """
    Task: Make requests to multiple URLs and collect status codes.
    URLs: ['https://httpbin.org/status/200', 'https://httpbin.org/status/201', 'https://httpbin.org/status/202']
    Store results in a dictionary: {url: status_code}
    """
    print("Exercise 8: Multiple Requests")
    print("-" * 40)
    
    urls = [
        'https://httpbin.org/status/200',
        'https://httpbin.org/status/201',
        'https://httpbin.org/status/202',
    ]
    
    # TODO: Your code here
    # 1. Create empty dictionary
    # 2. Loop through URLs
    # 3. Make request for each
    # 4. Store url: status_code in dictionary
    # 5. Print the dictionary
    
    print()

# ============================================================================
# SOLUTIONS (Uncomment to see answers)
# ============================================================================
"""
# SOLUTION 1
def exercise_1_solution():
    response = requests.get('https://httpbin.org/get')
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:100]}...")

# SOLUTION 2
def exercise_2_solution():
    urls = [
        'https://httpbin.org/status/200',
        'https://httpbin.org/status/404',
        'https://httpbin.org/status/500',
    ]
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url}: Success")
        else:
            print(f"{url}: Failed")

# SOLUTION 3
def exercise_3_solution():
    headers = {'User-Agent': 'MyScraper/1.0'}
    response = requests.get('https://httpbin.org/headers', headers=headers)
    print(response.text)

# SOLUTION 4
def exercise_4_solution():
    try:
        response = requests.get('https://httpbin.org/status/404')
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Request failed with HTTP error")

# SOLUTION 5
def exercise_5_solution():
    response = requests.get('https://httpbin.org/json')
    data = response.json()
    print(data['slideshow']['title'])

# SOLUTION 6
def exercise_6_solution():
    response = requests.get('https://httpbin.org/html')
    with open('exercise_output.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print("File saved!")

# SOLUTION 7
def exercise_7_solution():
    try:
        response = requests.get('https://httpbin.org/delay/5', timeout=2)
    except requests.exceptions.Timeout:
        print("Request timed out!")

# SOLUTION 8
def exercise_8_solution():
    urls = [
        'https://httpbin.org/status/200',
        'https://httpbin.org/status/201',
        'https://httpbin.org/status/202',
    ]
    results = {}
    for url in urls:
        response = requests.get(url)
        results[url] = response.status_code
    print(results)
"""

def main():
    """Run all exercises"""
    print("\n" + "=" * 60)
    print("HTTP REQUEST EXERCISES")
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
    
    print("=" * 60)
    print("Good luck! Check the solutions at the bottom of this file if stuck.")
    print("=" * 60)

if __name__ == "__main__":
    main()

