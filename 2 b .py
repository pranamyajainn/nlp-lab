import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Customer reviews
reviews = [
    "The product is very good and useful",
    "I am not happy with the product",
    "The quality is excellent"
]

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

for review in reviews:
    print("Original:", review)

    # Tokenization
    tokens = word_tokenize(review)
    print("Tokens:", tokens)

    # Stopword removal
    filtered = [w for w in tokens if w.lower() not in stop_words and w.isalpha()]
    print("Without Stopwords:", filtered)

    # Stemming
    stemmed = [stemmer.stem(w) for w in filtered]
    print("Stemmed:", stemmed)

    print()
