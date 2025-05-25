# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split on commas or spaces
        parts = re.split(r'[\s,]+', self.addresses.strip())
        
        # Simple regex to check for valid email format
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        
        # Filter to keep only valid emails
        valid_emails = [email for email in parts if email_pattern.match(email)]
        
        # Remove duplicates and sort
        return sorted(set(valid_emails))
