import re

text = "I like apples, bananas and mangoes, grapes too"

# Split but keep commas and spaces
tokens = re.split(r'([, ])', text)

# Separate words and separators
words = [t for t in tokens if t not in [' ', ','] and t != '']
separators = [t for t in tokens if t in [' ', ',']]

print("Words:", words)
print("Separators:", separators)
