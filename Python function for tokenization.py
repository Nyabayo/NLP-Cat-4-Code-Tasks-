import re

def tokenize_text(input_text):
    # Use regular expression to replace punctuation and special characters with a space
    cleaned_text = re.sub(r'[^\w\s]', ' ', input_text)
    
    # Split the text into tokens based on whitespace
    tokens = cleaned_text.split()
    
    return tokens

# Example usage
input_text = "Hello world! This is a test sentence; it includes: commas, periods, and other characters... like #hashtags and -dashes."
tokens = tokenize_text(input_text)
print(tokens)
