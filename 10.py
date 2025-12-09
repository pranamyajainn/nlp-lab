from nltk.util import bigrams
from collections import Counter
docs=["dog eats food","cat eats fish","dog likes cat"]
w=" ".join(docs).split()
b=list(bigrams(w))
c=Counter(b)
print("Count:",len(c))
print(c.most_common(5))
