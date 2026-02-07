"""
Test script to verify all required packages are installed correctly.
Run this after installing requirements.txt
"""

import sys

def test_import(module_name, package_name=None):
    """Test if a module can be imported."""
    try:
        __import__(module_name)
        if package_name:
            module = __import__(package_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"✓ {package_name} version: {version}")
        else:
            print(f"✓ {module_name} imported successfully")
        return True
    except ImportError as e:
        print(f"✗ {module_name} not found: {e}")
        return False

def main():
    print("Testing package installations...")
    print("-" * 50)
    
    all_ok = True
    
    # Test requests
    if test_import('requests'):
        try:
            import requests
            print(f"  → requests version: {requests.__version__}")
        except:
            pass
    else:
        all_ok = False
    
    # Test beautifulsoup4
    if test_import('bs4', 'bs4'):
        try:
            import bs4
            print(f"  → beautifulsoup4 version: {bs4.__version__}")
        except:
            pass
    else:
        all_ok = False
    
    # Test lxml
    if test_import('lxml'):
        try:
            import lxml
            print(f"  → lxml version: {lxml.__version__}")
        except:
            pass
    else:
        all_ok = False
    
    # Test built-in modules
    print("\nTesting built-in modules...")
    test_import('json')
    test_import('csv')
    test_import('xml.etree.ElementTree')
    
    print("-" * 50)
    if all_ok:
        print("\n✓ All packages installed successfully!")
        print("You're ready to start web scraping!")
        return 0
    else:
        print("\n✗ Some packages are missing.")
        print("Run: pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())

