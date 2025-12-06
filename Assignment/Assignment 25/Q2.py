import re

def extract_dates(text):
  
    patterns = [
        r"\b\d{2}/\d{2}/\d{4}\b",                   
        r"\b\d{2}-\d{2}-\d{4}\b",                     
        r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b"  # Month DD, YYYY
    ]
    
    dates = []
    for pattern in patterns:
        matches = re.findall(pattern, text)
        dates.extend(matches)
    
    return dates
sample_text = """
Important dates: 12/30/2025 is the deadline. 
We met on 30-11-2025. 
The project started on January 1, 2023.
"""

found_dates = extract_dates(sample_text)
print("Extracted Dates:", found_dates)