import nltk
from nltk import word_tokenize, pos_tag
from nltk.chunk import RegexpParser

# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input sentence
sentence = "The quick brown fox jumps over the lazy dog"

# Step 1: Tokenization
tokens = word_tokenize(sentence)

# Step 2: POS tagging
pos_tags = pos_tag(tokens)
print("POS Tags:")
print(pos_tags)

# Step 3: Define grammar
grammar = "NP: {<DT>?<JJ>*<NN>}"

# Step 4: Parse the sentence
parser = RegexpParser(grammar)
tree = parser.parse(pos_tags)

# Step 5: Draw parse tree
tree.draw()
