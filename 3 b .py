import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

# Given text
text = """
Natural Language Processing is a part of Artificial Intelligence.
It deals with the interaction between computers and humans
using natural language.
"""

# Step 1: Tokenization
tokens = word_tokenize(text.lower())

# Step 2: Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in tokens if w.isalpha() and w not in stop_words]

# Step 3: Count word frequency
word_freq = Counter(filtered_words)

# Step 4: Get most common words
words, counts = zip(*word_freq.most_common(5))

# Step 5: Plot graph
plt.bar(words, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Most Frequent Words")
plt.show()
