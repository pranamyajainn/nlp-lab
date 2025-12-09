import nltk
nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')
s="The dog ate the bone"
t=nltk.word_tokenize(s)
p=nltk.pos_tag(t)
print(p)
nltk.Tree.fromstring("(S (NP The dog) (VP ate (NP the
bone)))").draw() 
