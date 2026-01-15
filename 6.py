import re
import string
import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

# Download stopwords
nltk.download('stopwords')

# Given text
text = """
Follow us at https://twitter.com/openai and https://twitter.com/google.
AI research is growing fast and AI impacts technology.
"""

# Step 1: Extract Twitter handles
handles = re.findall(r'https://twitter\.com/(\w+)', text)
print("Twitter Handles:", handles)

# Step 2: Remove punctuation and convert to lowercase
clean_text = text.translate(str.maketrans('', '', string.punctuation)).lower()

# Step 3: Remove stopwords
stop_words = set(stopwords.words('english'))
words = clean_text.split()
filtered_words = [w for w in words if w not in stop_words]

# Step 4: Count word frequency
word_freq = Counter(filtered_words)

# Step 5: Plot bar graph
common_words = word_freq.most_common(5)
labels, counts = zip(*common_words)

plt.bar(labels, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Most Frequent Words")
plt.show()
