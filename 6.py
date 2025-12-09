from collections import Counter
t="a b a c"
w=t.split()
c=Counter(w)
V=len(c)
print({i:(c[i]+1)/(len(w)+V) for i in c})
