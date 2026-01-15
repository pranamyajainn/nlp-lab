import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

# Step 1: Create documents
doc1 = "Neural networks are powerful models"
doc2 = "Convolutional neural networks are used in vision"
doc3 = "Neural network layers contain neurons"

# Step 2: Combine documents
text = doc1 + " " + doc2 + " " + doc3

# Step 3: Tokenize and clean
tokens = word_tokenize(text.lower())
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in tokens if w.isalpha() and w not in stop_words]

# Step 4: Generate bigrams
bigrams = list(ngrams(filtered_words, 2))

# Step 5: Count bigram frequency
bigram_freq = Counter(bigrams)

print("Number of unique bigrams:", len(bigram_freq))

print("\nTop 5 most common bigrams:")
for bigram, freq in bigram_freq.most_common(5):
    print(bigram, "->", freq)
