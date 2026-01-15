import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Given text
text = "The cats are running quickly while the dogs were happily playing in the garden."

# Step 1: Tokenize
tokens = nltk.word_tokenize(text)

# Step 2: POS tagging
pos_tags = nltk.pos_tag(tokens)
print("POS Tags:")
print(pos_tags)

# Step 3: Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Step 4: POS conversion function
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

# Step 5: Lemmatization
lemmatized_words = [
    lemmatizer.lemmatize(word, get_wordnet_pos(tag))
    for word, tag in pos_tags
]

print("Lemmatized Words:")
print(lemmatized_words)
