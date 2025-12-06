import re

def validate_email(email):
    """
    Validate an email address using regex.
    Returns True if valid, False otherwise.
    """  
    pattern = re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )
    
    return bool(pattern.match(email))
emails = [
    "sanket@example.com",
    "user.name123@domain.co.in",
    "invalid-email@",
    "another@domain",
    "test@domain.com"
]

for e in emails:
    print(f"{e} -> {validate_email(e)}")