import re
from collections import defaultdict
import random

def preprocess_text(text):
    """Preprocess text by removing punctuation, making lowercase, and splitting into words."""
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    return words

def create_ngram_model(words, n):
    """Create an N-gram model from a list of words."""
    ngrams = defaultdict(lambda: defaultdict(lambda: 0))
    for i in range(len(words)-n+1):
        ngram = tuple(words[i:i+n-1])
        next_word = words[i+n-1]
        ngrams[ngram][next_word] += 1
    # Convert frequencies to probabilities
    for ngram, next_words in ngrams.items():
        total_count = sum(next_words.values())
        for next_word, count in next_words.items():
            ngrams[ngram][next_word] = count / total_count
    return ngrams

def generate_text(model, seed, num_words, n):
    """Generate text from an N-gram model given a seed phrase."""
    if len(seed.split()) < n-1:
        raise ValueError(f"Seed phrase must have at least {n-1} words.")
    
    current_ngram = tuple(seed.split()[-(n-1):])
    generated_words = list(current_ngram)
    
    for _ in range(num_words):
        if current_ngram not in model:
            break
        possible_words = list(model[current_ngram].keys())
        probabilities = list(model[current_ngram].values())
        next_word = random.choices(possible_words, weights=probabilities, k=1)[0]
        generated_words.append(next_word)
        current_ngram = tuple(generated_words[-(n-1):])
    
    return ' '.join(generated_words)

# Sample text to create the model
text = "This is an example text to illustrate how a simple N-gram model works. N-gram models are useful for text generation based on probability distributions of words."
words = preprocess_text(text)
n = 3  # You can experiment with different values of N for N-grams

# Create the N-gram model
model = create_ngram_model(words, n)

# Generate text with the model
seed_phrase = "this is"
num_words_to_generate = 20  # Number of words to generate
generated_text = generate_text(model, seed_phrase, num_words_to_generate, n)

print("Generated text:", generated_text)
