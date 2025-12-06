import re

def extract_urls(text):
    """
    Extract all URLs from the given text using regex.
    Returns a list of URLs.
    """
    
    url_pattern = re.compile(
        r"(https?://[^\s]+|www\.[^\s]+)",
        re.IGNORECASE
    )
    
    urls = re.findall(url_pattern, text)
    return urls


sample_text = """
Check out https://www.python.org for docs.
Visit my blog at www.example.com.
Secure site: https://secure-site.com/login
"""

found_urls = extract_urls(sample_text)
print("Extracted URLs:", found_urls)