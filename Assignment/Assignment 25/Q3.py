import re
from collections import Counter

def word_count(text):
    """
    Count occurrences of each word in the given text.
    Splits text into words using regex.
    """
    words = re.findall(r"\b\w+\b", text.lower())  
    
    freq = Counter(words)
    
    return freq
sample_text = "Python is great! Python is powerful, and Python is easy to learn."
result = word_count(sample_text)

print("Word Frequencies:")
for word, count in result.items():
    print(f"{word}: {count}")