import nltk, re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('punkt'); nltk.download('stopwords')
t="These are customer reviews about the product"
tok=nltk.word_tokenize(t)
sw=stopwords.words('english')
f=[w for w in tok if w.lower() not in sw]
ps=PorterStemmer()
st=[ps.stem(w) for w in f]
print(tok,f,st)
