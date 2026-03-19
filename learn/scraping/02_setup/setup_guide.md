# Step 2: Python Environment Setup

## Prerequisites

Before starting, make sure you have:
- Python 3.8 or higher installed
- A code editor (VS Code, PyCharm, or any text editor)
- Internet connection (for downloading packages)

## Step-by-Step Setup

### 1. Check Python Installation

Open your terminal/command prompt and run:
```bash
python --version
```

Or on some systems:
```bash
python3 --version
```

You should see something like: `Python 3.8.x` or higher.

**If Python is not installed:**
- Download from: https://www.python.org/downloads/
- During installation, check "Add Python to PATH"

### 2. Create a Virtual Environment (Recommended)

A virtual environment keeps your project dependencies separate from other projects.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You'll know it's activated when you see `(venv)` at the start of your terminal prompt.

### 3. Install Required Packages

With your virtual environment activated, run:
```bash
pip install -r requirements.txt
```

This will install:
- `requests` - For making HTTP requests
- `beautifulsoup4` - For parsing HTML
- `lxml` - Fast XML/HTML parser

### 4. Verify Installation

Run the test script:
```bash
python 02_setup/test_installation.py
```

If everything is installed correctly, you should see:
```
✓ All packages installed successfully!
✓ requests version: 2.x.x
✓ beautifulsoup4 version: 4.x.x
✓ lxml version: 4.x.x
```

## Troubleshooting

### Issue: "python is not recognized"
**Solution:** Make sure Python is added to your PATH, or use `python3` instead of `python`

### Issue: "pip is not recognized"
**Solution:** Try `python -m pip` instead of just `pip`

### Issue: Permission errors on Mac/Linux
**Solution:** Use `pip3 install --user` or activate your virtual environment first

### Issue: Virtual environment won't activate
**Solution:** 
- Windows: Try `.\venv\Scripts\activate` or use PowerShell instead of CMD
- Mac/Linux: Make sure you're in the project directory

## Basic Python Concepts You'll Need

### Lists
```python
items = ['apple', 'banana', 'cherry']
print(items[0])  # Output: apple
```

### Dictionaries
```python
person = {
    'name': 'John',
    'age': 30
}
print(person['name'])  # Output: John
```

### File I/O
```python
# Reading a file
with open('file.txt', 'r') as f:
    content = f.read()

# Writing a file
with open('output.json', 'w') as f:
    f.write('{"key": "value"}')
```

### Error Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## Next Steps

Once your environment is set up:
1. Run `test_installation.py` to verify everything works
2. Move to Step 3: Making HTTP Requests
3. Start practicing with the `requests` library

---

**Tip:** Keep your virtual environment activated while working on this project. If you close your terminal, you'll need to activate it again.

