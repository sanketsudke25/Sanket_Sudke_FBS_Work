import re

def censor_text(text, forbidden_words):
    """
    Replace all occurrences of forbidden words with asterisks (*).
    """
    for word in forbidden_words:
       
        pattern = re.compile(rf"\b{word}\b", re.IGNORECASE)
        text = pattern.sub("*" * len(word), text)
    return text
sample_text = "Python is powerful but some people misuse Python for hacking."
forbidden = ["python", "hacking"]

censored = censor_text(sample_text, forbidden)
print("Original:", sample_text)
print("Censored:", censored)